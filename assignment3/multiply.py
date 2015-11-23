import MapReduce
import sys

"""
Sparse matrix multiplication using MapReduce Model thinking
"""

mr = MapReduce.MapReduce()
# Predetermine output matrix size
A_row = 5
B_col = 5
M = 5

def mapper(record):
    if record[0] == 'a':
        for k in range(A_row):
            key = (record[1], k)
            value = {record[2] : record[-1]}
            mr.emit_intermediate(key, value)
    else:
        for k in range(B_col):
            key = (k, record[2])
            value = {record[1] : record[-1]}
            mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    total = 0
    #sorted_values = sorted(list_of_values,key=lambda x: x.keys())
    for j in range(M):
        values = [elem.values() for elem in list_of_values if elem.keys()==[j]]
        if len(values) == 2:
            total += values[0][0]*values[1][0]
    emit_list = list(key)
    emit_list.append(total)
    mr.emit(tuple(emit_list))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)