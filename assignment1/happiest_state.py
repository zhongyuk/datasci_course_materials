import sys
import json

#===Functions not directly called by main(), but nested inside functions called by main()
def identify_state(place):
    from string import upper, strip
    states = {'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AS': 'American Samoa',
    'AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut',
    'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia',
    'GU': 'Guam','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
    'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts',
    'MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri',
    'MP': 'Northern Mariana Islands','MS': 'Mississippi','MT': 'Montana','NA': 'National','NC': 'North Carolina',
    'ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey',
    'NM': 'New Mexico','NV': 'Nevada','NY': 'New York','OH': 'Ohio','OK': 'Oklahoma',
    'OR': 'Oregon','PA': 'Pennsylvania','PR': 'Puerto Rico','RI': 'Rhode Island',
    'SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas',
    'UT': 'Utah','VA': 'Virginia','VI': 'Virgin Islands','VT': 'Vermont',
    'WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}
    words = place.split(',')
    words = map(upper, words)
    words = map(strip, words)
    state_terms = states.keys()+states.values()
    state_terms = map(upper, state_terms)
    state_terms = map(unicode, state_terms) ## not necessary
    state = set(words) & set(state_terms)
    if state == set():
        state = None
    else:
        state = list(state)[0]
        if len(state) > 2:
            state = std_state(state)
    return state

def find_state(coord):
    # state_coordiantes value order: west bound, east bound, north bound, south bound
    state_coord = {'Alabama':[-88.5,-84.87,35.0,30.25],
    'Alaska':[173.5,-130,71.5,51.25], 'Arizona':[-114.87,-109,37.0,31.33],
    'Arkansas':[-94.62,-89.62,36.5,33], 'California':[-124.42,-114.12,42,32.5],
    'Colorado': [-109.12,-102,41,37], 'Connecticut':[-73.75,-71.75,42.05,41],
    'Delaware': [-75.8,-75,39.85,38.45], 'District of Columbia':[-77.12,-76.87,39,38.87],
    'Florida':[-87.62,-80,31,24.5], 'Georgia':[-85.62,-80.75,35,30.35],
    'Hawaii':[-160.25,-154.75,22.23,18.87], 'Idaho':[-117.25,-111,49,42],
    'Illinois':[-91.5,-87.5,42.5,37], 'Indiana':[-88.12,-84.75,41.75,37.87],
    'Iowa':[-96.62,-90.12,43.5,40.37], 'Kansas':[-102.5,-94.58,40,37],
    'Kentucky':[-89.58,-81.95,39.15,36.62],'Louisiana':[-94.05,-88.82,33.02,28.92],
    'Maine':[-71.13,-66.88,47.47,42.97], 'Maryland':[-79.5,-75,39.75,37.87],
    'Massachusetts':[-73.5,-69.92,42.87,41.22], 'Michigan':[-90.5,-82.37,48.28,41.7],
    'Minnesota':[-97.25,-89.5,49.38,43.5], 'Mississippi':[-91.63,-88.12,35,30],
    'Missouri':[-95.78,-89.1,40.62,36], 'Montana':[-116.05,-102.03,49,44.37],
    'Nebraska':[-104.05,-95.15,43,40], 'Nevada':[-120,-114.05,42,35],
    'New Hampshire':[-72.57,-70.58,45.35,42.7], 'New Jersey':[-75.55,-70.58,45.35,42.7],
    'New Mexico':[-109.05,-103,37,31.33], 'New York':[-79.77,-71.87,45,40.5],
    'North Carolina':[-84.33,-75.42,36.6,33.85], 'North Dokota':[-104.05,-96.55,49,45.93],
    'Ohio':[-84.82,-80.5,42,38.4], 'Oklahoma':[-103,-94.43,37,33.62],
    'Oregon':[-124.58,-116.45,46.27,42], 'Pennsylvania':[-80.5,-74.68,42.27,39.72],
    'Puerto Rico':[-67.95,-65.22,18.53,17.92], 'Rhode Island':[-71.92,-71.12,42,41.13],
    'South Carolina':[-83.37,-78.5,35.22,32], 'South Dokota':[-104.05,-96.43,45.93,42.48],
    'Tennessee':[-90.32,-81.63,36.68,34.97], 'Texa':[-105.65,-93.5,36.5,25.83],
    'Utah':[-114.05,-109,42,37], 'Vermont':[-73.6,-71.47,45,42.72],
    'Vermont':[-73.6,-71.47,45,42.72], 'Virgin Islands':[-64.8,-64.55,18.42,17.67],
    'Virginia':[-83.68,-75.25,39.47,36.53], 'Washington':[-124.77,-116.92,49,45.53],
    'West Virginia':[-83.65,-77.73,40.63,37.2], 'Wisconsin':[-92.9,-86.75,47.12,42.5],
    'Wyoming':[-111.1,-104,45,41]}
    for key in state_coord.keys():
        if (coord[0] <= state_coord[key][1]) & (coord[0] >= state_coord[key][0]):
            if (coord[1] <= state_coord[key][2]) & (coord[1] >= state_coord[key][3]):
                state = key
                state = std_state(state)
                break
        else:
            state = None
    return state

def std_state(state):
    from string import upper
    abbreviation = state
    states = {'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AS': 'American Samoa',
    'AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut',
    'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia',
    'GU': 'Guam','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
    'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts',
    'MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri',
    'MP': 'Northern Mariana Islands','MS': 'Mississippi','MT': 'Montana','NA': 'National','NC': 'North Carolina',
    'ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey',
    'NM': 'New Mexico','NV': 'Nevada','NY': 'New York','OH': 'Ohio','OK': 'Oklahoma',
    'OR': 'Oregon','PA': 'Pennsylvania','PR': 'Puerto Rico','RI': 'Rhode Island',
    'SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas',
    'UT': 'Utah','VA': 'Virginia','VI': 'Virgin Islands','VT': 'Vermont',
    'WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}
    for k,v in states.items():
        if upper(v) == upper(state):
            abbreviation = k
            break
    return abbreviation

def strip_special_char(string):
    import re
    remain_exp = re.compile('[^a-zA-Z0-9\s]')
    string_strip = remain_exp.sub(' ',string)
    return string_strip

#=== Functions called directly in main()
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
        scores = find_word_score(tweet_dict[tweet], term_sentiment)
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

def extract_coordinates(tweet_file_handler):
    tweet_coordinates = {}
    for line in tweet_file_handler:
        stream = json.loads(line)
        tweet = stream.get(u'text', None)
        if tweet != None:
            coordinate = stream.get(u'coordinates', None)
            if coordinate != None:
                coordinate_values = coordinate.get(u'coordinates')
                tweet_coordinates[tweet] = coordinate_values
            else:
                tweet_coordinates[tweet] = None
    return tweet_coordinates

def extract_places(tweet_file_handler):
    tweet_places = {}
    for line in tweet_file_handler:
        stream = json.loads(line)
        tweet = stream.get(u'text', None)
        if tweet != None:
            place = stream.get(u'place', None)
            if place != None:
                country = place.get(u'country_code')
                if country == u'US':
                    location = place.get(u'full_name')
                    tweet_places[tweet] = location
                else:
                    tweet_places[tweet] = None
            else:
                tweet_places[tweet] = None
    return tweet_places

def extract_users(tweet_file_handler):
    tweet_users = {}
    for line in tweet_file_handler:
        stream = json.loads(line)
        tweet = stream.get(u'text', None)
        if tweet != None:
            user = stream.get(u'user', None)
            if user != None:
                location = user.get(u'location')
                tweet_users[tweet] = location
            else:
                tweet_users[tweet] = user
    return tweet_users

def match_coord_states(tweet_coordiantes):
    tweet_coord_state = {}
    # coordinate is longitude (East-West) first, then latitude (North-South)
    for tweet, coord in tweet_coordiantes.items():
        if (coord != None):
            if (coord[1]>15) & (coord[0]<0): # Roughly check if coord is in USA
                tweet_coord_state[tweet] = find_state(coord)
            else:
                tweet_coord_state[tweet] = None
        else:
            tweet_coord_state[tweet] = None
    return tweet_coord_state
 
def extract_states(tweet_geo):
    tweet_state = {}
    for tweet, geo in tweet_geo.items():
        if geo != None:
            tweet_state[tweet] = identify_state(geo)
        else:
            tweet_state[tweet] = None
    return tweet_state

def determine_state(coord, place, user):
    # Reliable level order: coord > place > user
    tweet_state = {}
    for tweet in coord.keys():
        if coord[tweet] == None:
            if place[tweet] == None:
                tweet_state[tweet] = user[tweet]
            else:
                tweet_state[tweet] = place[tweet]
        else:
            tweet_state[tweet] = coord[tweet]
    return tweet_state

def calc_state_avg_sentiment(tweet_sentiment, tweet_state):
    state_sum_count = {}
    for tweet, state in tweet_state.items():
        if state != None:
            if state_sum_count.get(state,-1) == -1:
                state_sum_count[state]={'sum':tweet_sentiment[tweet],'count':1}
            else:
                state_sum_count[state]['sum'] += tweet_sentiment[tweet]
                state_sum_count[state]['count'] += 1
    state_avg_sent = {k: float(v['sum'])/v['count'] for k, v in state_sum_count.items()}
    return state_avg_sent

def std_print(state_avg_sentiment):
    sorted_input = sorted(state_avg_sentiment.items(),key=lambda x:x[1], reverse=True)
    print sorted_input[0][0]

def main():
    tweet_file_name = sys.argv[2] #"output.txt" #
    sent_file_name = sys.argv[1] #"AFINN-111.txt" #
    #=== Extract and Compute Tweet - Sentiment
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
    #=== Extract Tweet - Location/State
    # * Extract tweet - coordinate fields (a dictionary)
    with open(tweet_file_name) as tweet_file:
        tweet_coordinates = extract_coordinates(tweet_file)
    # * Extract tweet - place fields (a dictionary)
    with open(tweet_file_name) as tweet_file:
        tweet_places = extract_places(tweet_file)
    # * Extract tweet - user fields (a dicitonary):
    with open(tweet_file_name) as tweet_file:
        tweet_users = extract_users(tweet_file)
    # Match coordiantes to states
    tweet_coord_state = match_coord_states(tweet_coordinates)
    # Extract state info based on place field and user field
    tweet_place_state = extract_states(tweet_places)
    tweet_user_state = extract_states(tweet_users)
    # Incorporate geo info extracted from 3 different fields
    tweet_state = determine_state(tweet_coord_state, tweet_place_state, tweet_user_state)
    # Compute state - average_tweet_sentiment pairs (a dictionary)
    state_avg_sentiment = calc_state_avg_sentiment(tweet_sentiment, tweet_state)
    # Compare and print out the happiest state to standard output
    std_print(state_avg_sentiment)
    

if __name__ == "__main__":
    main()

