import sys
import json

def hw():
	 print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def extract_tweets(tweet_file_handler):
    tweet_data = list()
    for line in tweet_file_handler:
        stream = json.loads(line)
        tweet = stream.get(u'text', None)
        tweet_data.append(tweet)
    return tweet_data

def extract_term_sentiment(sent_file_handler):
    term_sentiment = {}
    for line in sent_file_handler:
        term, score = line.split("\t")
        term_sentiment[term] = int(score)
    return term_sentiment

def build_tweet_dict(tweet_data):
    from collections import OrderedDict
    tweet_dict = OrderedDict()
    for tweet in tweet_data:
        if tweet != None:
            tweet_strip = strip_special_char(tweet)
            words = tweet_strip.split()
            #words = map(strip_special_char, words)
            words = map(unicode, words)
            tweet_dict[tweet] = words
    return tweet_dict
    
def calc_tweet_sentiment(tweet_dict, term_sentiment):
    tweet_sentiment = {}
    for tweet in tweet_dict.keys():
        words_list = map(strip_special_char, tweet_dict[tweet])
        scores = find_word_score(words_list, term_sentiment)
        sentiment = sum(scores)
        print str(sentiment)
        tweet_sentiment[tweet] = sentiment
    return tweet_sentiment

def strip_special_char(string):
    import re
    remain_exp = re.compile('[^a-zA-Z0-9\s]')
    string_strip = remain_exp.sub(' ',string)
    return string_strip

def find_word_score(word_list, term_sentiment):
    scores = list()
    for word in word_list:
        score = term_sentiment.get(word, 0)
        scores.append(score)
    return scores
    
def main():
    sent_file_name =  sys.argv[1]#'output.txt' #sys.argv[1] #
    tweet_file_name = sys.argv[2]#'AFINN-111.txt' #sys.argv[2] #
    # * Skeleton provided originally
    #with open(tweet_file_name) as tweet_file:
    #lines(tweet_file)
        #with open(sent_file_name) as  sent_file:
        #lines(sent_file)
    #hw()
    # * Extract Tweets
    with open(tweet_file_name) as tweet_file:
        tweet_data = extract_tweets(tweet_file)
    # * Extract term sentiment pair dictionary
    with open(sent_file_name) as sent_file:
        term_sentiment = extract_term_sentiment(sent_file)
    # * Build a tweet - terms pair (a dictionary)
    tweet_dict = build_tweet_dict(tweet_data)
    # * Compute the score of tweets
    tweet_sentiment = calc_tweet_sentiment(tweet_dict, term_sentiment)
    
if __name__ == "__main__":
    main()