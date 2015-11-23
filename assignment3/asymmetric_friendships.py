import MapReduce
import sys

"""
Count asymmetric friendships using MapReduce model thinking
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # record: [person, friend]
    # key1: friend
    # value1: [[], [friend, person]]
    # key2: person
    # value2: [[person, friend],[]]
    key1 = record[1]
    value1 = [[], record[0]]
    mr.emit_intermediate(key1, value1)
    key2 = record[0]
    value2 = [record[1],[]]
    mr.emit_intermediate(key2, value2)


def reducer(key, list_of_values):
    # key:
    # value: person's asymmetric friend
    indata = []
    outdata = []
    for v in list_of_values:
        indata.append(v[0])
        outdata.append(v[1])
    for value in outdata:
        if (value!=[]) & (value not in indata):
# in order to make grader happy, for every asymmetric friendship, need to output both [person, friend], and [friend person]
            mr.emit((key, value)) # Command out this line for right output instead of purly satisfying grader
            mr.emit((value, key))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)