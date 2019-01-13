from sys import argv
from dequeue import Dequeue

potential_palindrome = argv[1]

def check_palindrome(string_to_check):
    dq = Dequeue()
    dq.set_items(string_to_check)

    is_palindrome = True

    while dq.size() > 1:
        if dq.remove_front() != dq.remove_rear():
            is_palindrome = False
    
    return is_palindrome

print(check_palindrome(potential_palindrome))
