import string

class Dequeue:
    def __init__(self):
        self._items = []
        self._allowed_chars = list(string.ascii_lowercase)
        self._uppercase_list = {
            'A':'a',
            'B':'b',
            'C':'c',
            'D':'d',
            'E':'e',
            'F':'f',
            'G':'g',
            'H':'h',
            'I':'i',
            'J':'j',
            'K':'k',
            'L':'l',
            'M':'m',
            'N':'n',
            'O':'o',
            'P':'p',
            'Q':'q',
            'R':'r',
            'S':'s',
            'T':'t',
            'U':'u',
            'V':'v',
            'W':'w',
            'X':'x',
            'Y':'y',
            'Z':'z',
        }

    def set_items(self, string):
        items = list(string)
        for item in items:
            if item in self._allowed_chars:
                self.add_rear(item)
            elif self._uppercase_list.get(item):
                self.add_rear(self._uppercase_list.get(item))

        print (self._items)

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
 


    