import MapReduce
import sys

"""
trim and output unique nucleotides using MapReduce model thinking
"""
mr = MapReduce.MapReduce()

def mapper(record):
    key = 'seq_id'
    value = record[1][:-10]
    mr.emit_intermediate(key,value)


def reducer(key, list_of_values):
    values = list(set(list_of_values))
    for v in values:
        mr.emit((v))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)