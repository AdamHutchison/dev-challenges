import string

class Dequeue:
    def __init__(self):
        self._items = []

    def set_items(self, string):
        items = list(string)
        for item in items:
            if ord(item) in range(ord('a'), ord('z') + 1):
                self.add_rear(item)
            elif ord(item) in range(ord('A'), ord('Z') + 1): 
                # difference between upper case and lowercase ascii valies is +32
                self.add_rear(chr(ord(item) + 32))

    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        if self._items:
           return self._items.pop(0)

    def remove_rear(self):
        if self._items:
            return self._items.pop()

    def peek_front(self):
        if self._items:
            return self._items[0]

    def peek_rear(self):
        if self._items:
            return self._items[-1]

    def size(self):
        return len(self._items)
        
    def is_empty(self):
        return len(self._items) == 0
 


    