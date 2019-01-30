from point import Point

class MatrixSearcher:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def point_exists(self, point):
        return 

    def find_element(self, origin, dest, element):
        if not self.__check_in_bounds(origin, dest):
            return
        # check if the origin is the element we're tring to find
        if self.matrix[origin.row][origin.column] == element:
            return origin
        
        start = origin.clone()
        diagDist = min(dest.row - origin.row, dest.column - origin.column)
        end = Point(start.row + diagDist, start.column + diagDist)

        current_point = Point(0, 0)

        while start.is_before(end):
            current_point.set_to_average(start, end)
            if element > self.matrix[current_point.row][current_point.column]:
                start.row = current_point.row + 1
                start.column = current_point.column + 1
            else:
                end.row = current_point.row - 1
                end.column = current_point.column - 1

        return self.__partition_and_search(origin, dest, start, element)
        
    def __partition_and_search(self, origin, dest, pivot, element):
        lower_left_origin = Point(pivot.row, origin.column)
        lower_left_dest = Point(dest.row, pivot.column - 1)
        upper_right_origin = Point(origin.row, pivot.column)
        upper_right_dest = Point(pivot.row - 1, dest.column)

        lower_left = self.find_element(lower_left_origin, lower_left_dest, element)

        if not lower_left:
            return self.find_element(upper_right_origin, upper_right_dest, element)
        
        return lower_left
    
    def __check_in_bounds(self, origin, dest):
       # handle situations when element is not found by binary search
        if not origin.in_bounds(self.matrix) or not dest.in_bounds(self.matrix):
            return False
        elif not origin.is_before(dest):
            return False

        return True
        