from sys import argv

n = int(argv[1])

def main():
    print(countSteps(n))

def countSteps(n, cachedValues = {}):
    if n < 0: 
        return 0
    elif n == 0: 
        return 1
    elif cachedValues.get(n) != None:
        # print(f"cached values used for when n = {n}")
        return cachedValues.get(n)
    else:
        # print(f"This ran for n = {n}")
        cachedValues[n] = countSteps(n-1, cachedValues) + countSteps(n-2, cachedValues) + countSteps(n-3, cachedValues)
        # print(cachedValues)
        return cachedValues[n]

if __name__ == "__main__":
    main()