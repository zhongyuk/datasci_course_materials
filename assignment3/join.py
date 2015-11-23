import MapReduce
import sys

"""
MapReduce Model thinking, sql join operateion example
"""
mr = MapReduce.MapReduce()


def mapper(record):
    # Key for mapper and reducer is join key, the order_id
    # Value for mapper and reducer is the rest table info
    key = record[1]
    value = record
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    list_of_len = map(len,list_of_values)
    order_index = [i for i, v in enumerate(list_of_len) if v == 10]
    lineitem_index = [i for i, v in enumerate(list_of_len) if v==17]
    Order = [list_of_values[i] for i in order_index]
    LineItem = [list_of_values[i] for i in lineitem_index]
    for o in Order:
        for l in LineItem:
            output = o + l
            mr.emit(output)


if __name__ == "__main__":
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
