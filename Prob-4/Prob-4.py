# Module 2
#   Programming Assignment 3
#     Prob-4.py

# Trevor Bromley
from random import *

def main():
    print("\nTrevor's Output")
    
    sum = 0
    for i in range(5):
        num = randrange(1,100)
        print(num)
        sum = sum + num
    print("---------")
    print("sum: ", sum)


main()
