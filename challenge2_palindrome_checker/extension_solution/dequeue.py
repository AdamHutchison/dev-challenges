class Dequeue:
    def __init__(self):
        self._items = []
    
    def set_items(self, string):
        self.items = list(string)
    
    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
           return self.items.pop(0)

    def remove_rear(self):
        if self.items:
            return self.items.pop()

    def peek_front(self):
        if self.items:
            return self.items[0]

    def peek_rear(self):
        if self.items:
            return self.items[-1]

    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return len(self.items) == 0


    