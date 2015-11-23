import sys
import json

def extract_tweets(tweet_file_handler):
    tweet_data = list()
    for line in tweet_file_handler:
        stream = json.loads(line)
        tweet = stream.get(u'text', None)
        tweet_data.append(tweet)
    return tweet_data

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

def calc_term_freq(tweet_dict):
    words_nested_list = tweet_dict.values()
    # unnest lists
    words_list = sum(words_nested_list, [])
    # strip non-alphebetic and non digits
    words_list = map(strip_special_char, words_list)
    from collections import Counter
    word_counts = Counter()
    for word in words_list:
        word_counts += Counter({word: 1})
    word_counts = dict(word_counts)
    total_counts = float(sum(word_counts.values()))
    word_freq = {k: v/total_counts for k, v in word_counts.items()}
    return word_freq

def print_stdout(print_dict):
    for key in print_dict.keys():
        print key.encode('utf-8')+" "+str(print_dict[key])

def strip_special_char(string):
    import re
    remain_exp = re.compile('[^a-zA-Z0-9\s]')
    string_strip = remain_exp.sub(' ',string)
    return string_strip

def main():
    tweet_file_name =  sys.argv[1] #"output.txt"#
    # * Extract Tweets
    with open(tweet_file_name) as tweet_file:
        tweet_data = extract_tweets(tweet_file)
    # * Extract term sentiment pair dictionary
    #with open(sent_file_name) as sent_file:
    #term_sentiment = extract_term_sentiment(sent_file)
    # * Build a tweet - terms pair (a dictionary)
    tweet_dict = build_tweet_dict(tweet_data)
    # * Compute term frequency
    term_freq = calc_term_freq(tweet_dict)
    # * Print term_freq into standard output
    print_stdout(term_freq)

if __name__ == "__main__":
    main()