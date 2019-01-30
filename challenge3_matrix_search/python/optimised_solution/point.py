from copy import deepcopy

class Point:
    def __init__(self, row, column):
        self.column = column
        self.row = row

    def in_bounds(self, matrix):
        return self.row >= 0 and self.column >= 0 \
        and self.row < len(matrix) and self.column < len(matrix[0])

    def is_before(self, point):
        return self.row <= point.row and self.column <= point.column

    def set_to_average(self, min_point, max_point):
        self.row = (min_point.row + max_point.row) // 2
        self.column = (min_point.column + max_point.column) // 2
    
    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"[{self.row}, {self.column}]"