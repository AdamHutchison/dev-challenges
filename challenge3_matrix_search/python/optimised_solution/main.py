from point import Point
from matrixsearcher import MatrixSearcher
from sys import argv
import numpy as np
import time

element_to_search_for = int(argv[1])

matrix = np.arange(100000000).reshape(10000, 10000)
# [
#     [0, 1, 2, 3,],
#     [4, 5, 6, 7],
#     [8, 9, 10, 11],
#     [12, 13, 14, 15],
#     [16, 17, 18, 19],
# 

def main(matrix, element):
    origin = Point(0, 0)
    dest = Point(len(matrix) - 1, len(matrix[0]) - 1)
    search = MatrixSearcher(matrix)

    print(search.find_element(origin, dest, element))


if __name__ == "__main__":
    start_time = time.time()
    main(matrix, element_to_search_for)
    print("--- %s seconds ---" % (time.time() - start_time))