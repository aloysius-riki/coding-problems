"""
Given a list of numbers ordered in ascending order, write a function called missingNumbers
in Python that finds the missing
numbers in the list. For instance, if the first list is [1,2,6,7,10], the function
will return [3,4,5,8,9].
"""

import sys

def missingNumbers(numbers):
    missingNumbersList = []
    numbers = [int(x) for x in numbers]
    numbers.sort()
    for i in range(1, numbers[-1] + 1):
        if i not in numbers:
            missingNumbersList.append(i)
    return missingNumbersList

def main():
    numbers = sys.argv[1:]
    print(missingNumbers(numbers))

if __name__ == '__main__':
    main()