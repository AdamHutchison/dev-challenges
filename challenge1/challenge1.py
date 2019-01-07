from sys import argv

n = int(argv[1])

def countSteps(n):
    if (n < 0): 
        return 0
    elif (n == 0): 
        return 1
    else:
        return countSteps(n-1) + countSteps(n-2) + countSteps(n-3)
        
print(countSteps(n))