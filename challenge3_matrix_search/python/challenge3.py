from sys import argv
from binarysearcher import BinarySearcher

element = int(argv[1])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
]

def matrix_search(element):
    row = 0
    while row <= len(matrix) -1:
        search = BinarySearcher(matrix[row])
        value = search.find_element(element)
        if(value != 'Not Found'):
            return [row, value]
        
        row += 1
    
    return "Not Found"

print(matrix_search(element))

