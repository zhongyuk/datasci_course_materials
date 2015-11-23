import MapReduce
import sys

"""
MapReduce Model thinking, simple social network analysis - friend count example
"""
mr = MapReduce.MapReduce()

def mapper(record):
    # Key for mapper and reducer is people's name
    # Value for mapper and reducer is friend count
    key = record[0]
    value = 1
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)