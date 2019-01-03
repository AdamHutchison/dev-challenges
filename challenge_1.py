from sys import argv

n = int(argv[1])

def main():
    print(countSteps(n))

def countSteps(n):
    if (n == 1 or n == 0): 
        return 1
    elif (n == 2): 
        return 2
    else:
        return countSteps(n-1) + countSteps(n-2) + countSteps(n-3)

if __name__ == "__main__":
    main()