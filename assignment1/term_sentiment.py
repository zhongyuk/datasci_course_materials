import sys
import json

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
    from string import lower
    tweet_dict = OrderedDict()
    for tweet in tweet_data:
        if tweet != None:
            tweet_strip = unicode(strip_special_char(tweet))
            words = tweet_strip.split()
            words = map(lower, words)
            #words = map(unicode, words)
            #print words
            tweet_dict[tweet] = words
    return tweet_dict
    
def calc_tweet_sentiment(tweet_dict, term_sentiment):
    from collections import OrderedDict
    tweet_sentiment = OrderedDict()
    for tweet in tweet_dict.keys():
        words_list = map(strip_special_char, tweet_dict[tweet])
        scores = find_word_score(words_list, term_sentiment)
        sentiment = sum(scores)
        #print str(sentiment)
        tweet_sentiment[tweet] = sentiment
    return tweet_sentiment

def find_word_score(word_list, term_sentiment):
    scores = list()
    for word in word_list:
        score = term_sentiment.get(word, 0)
        scores.append(score)
    return scores

def deduce_word_sentiment(tweet_dict, tweet_sentiment, term_sentiment):
    from collections import Counter
    word_sentiment = Counter()
    terms = term_sentiment.keys()
    terms = map(lambda x: unicode(x,encoding='utf-8'),terms)
    for tweet in tweet_dict.keys():
        words = sorted(set(tweet_dict[tweet]))
        if len(words)>0: # words can be empty when tweets are in non-English language
            weight = float(tweet_sentiment[tweet])/len(words)
            for word in words:
                if word not in terms:
                    word_sentiment.update({word: weight})
    return dict(word_sentiment)

def strip_special_char(string):
    import re
    remain_exp = re.compile('[^a-zA-Z0-9\s]')
    string_strip = remain_exp.sub(' ',string)
    return string_strip

def print_stdout(word_sentiment):
    for word in word_sentiment.keys():
        print word.encode('utf-8')+" "+str(word_sentiment[word])

def main():
    #-----------------Same as tweet_sentiment--------------------------
    sent_file_name = sys.argv[1] #"AFINN-111.txt" #
    tweet_file_name = sys.argv[2] #"output.txt" #
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
    #------------------------------------------------------------------
    # * Compute word - sentiment pair (a dictionary)
    word_sentiment = deduce_word_sentiment(tweet_dict, tweet_sentiment, term_sentiment)
    # * Print deducted word_sentiment as standard output
    print_stdout(word_sentiment)
    
     
if __name__ == "__main__":
    main()