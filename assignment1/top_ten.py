import sys
import json

def count_hashtags(tweet_file):
    hashtag_count = {}
    for line in tweet_file:
        stream = json.loads(line)
        entity = stream.get(u'entities', None)
        if entity != None:
            hashtag = entity.get(u'hashtags')
            if hashtag != []:
                hashtag_txt = hashtag[0].get("text")
                if hashtag_count.get(hashtag_txt, -1)==-1:
                    hashtag_count[hashtag_txt] = float(1)
                else:
                    hashtag_count[hashtag_txt] += float(1)
    return hashtag_count

def print_top_ten(hashtag_count):
    sorted_hashtag = sorted(hashtag_count.items(),
    key=lambda x:x[1], reverse = True)
    for i in range(10):
        print sorted_hashtag[i][0].encode('utf-8')+' '+str(sorted_hashtag[i][1])

def main():
    tweet_file_name = sys.argv[1] #'output.txt' #
    with open(tweet_file_name) as tweet_file:
        hashtag_count = count_hashtags(tweet_file)
    # sort hashtag - count pairs, print top ten hash tags to stdout
    print_top_ten(hashtag_count)

if __name__ == "__main__":
    main()