class BinarySearcher:
    def __init__(self, values):
        self.values = values
        self.upper = len(values) - 1
        self.lower = 0
        self.midpoint = self.upper // 2
    
    def find_element(self, element):
        while self.lower <= self.upper:
            self.midpoint = (self.lower + self.upper) // 2
            if(element == self.values[self.midpoint]):
                return self.midpoint
            elif(element < self.values[self.midpoint]):
                self.adjust_upper()
            elif(element > self.values[self.midpoint]):
                self.adjust_lower()
        
        return "Not Found"
    
    def adjust_upper(self):
        self.upper = self.midpoint - 1

    def adjust_lower(self):
        self.lower = self.midpoint + 1