from sys import argv
from dequeue import Dequeue
import re

potential_palindrome = argv[1]

def check_palindrome(string_to_check):
    sanitised_string = re.sub("[^a-zA-Z]","", string_to_check).lower()
    
    dq = Dequeue()
    dq.set_items(sanitised_string)

    is_palindrome = True

    while dq.size() > 1:
        if dq.remove_front() != dq.remove_rear():
            is_palindrome = False
    
    return is_palindrome

print(check_palindrome(potential_palindrome))
