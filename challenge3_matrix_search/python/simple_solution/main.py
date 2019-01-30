from sys import argv
from binarysearcher import BinarySearcher
import numpy as np
import time

element = int(argv[1])

# matrix = np.arange(20).reshape(5, 4)
# [
#     [0, 1, 2, 3,],
#     [4, 5, 6, 7],
#     [8, 9, 10, 11],
#     [12, 13, 14, 15],
#     [16, 17, 18, 19],
# ]

matrix = np.arange(100000000).reshape(10000, 10000)

def matrix_search(element):
    for row in range(len(matrix)):
        search = BinarySearcher(matrix[row])
        value = search.find_element(element)
        if(value != None):
            return [row, value]

    return "Not Found"

start_time = time.time()
print(matrix_search(element))
print("--- %s seconds ---" % (time.time() - start_time))

