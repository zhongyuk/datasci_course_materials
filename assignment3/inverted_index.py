import MapReduce
import sys

"""
MapReduce Model thinking, inverted index example
"""
mr = MapReduce.MapReduce()

# ======Functions for strip special characters==============
def strip_special_char(string):
    import re
    remain_exp = re.compile("[^'a-zA-Z0-9\s]")
    string_strip = remain_exp.sub(' ',string)
    return string_strip

def extract_contraction(string):
    # for dealing with contraction
    if string.startswith("'") | string.endswith("'"):
        output = string.strip("'")
    else:
        output = string
    return output
# ==========================================================

def mapper(record):
    # Key for mapper and reducer is word in each record
    # Value for mapper and reducer is a list of doc_ids
    doc_id = record[0]
    text = record[1]#.lower()
    #text = strip_special_char(text)
    words = text.split()
    #words = map(extract_contraction,words)
    words = list(set(words)) # Remove duplicates
    for word in words:
        mr.emit_intermediate(word, doc_id)

def reducer(key, list_of_values):
    mr.emit((key, list_of_values))
    
if __name__ == "__main__":
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)