#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    listLength = len(a) - 1
    counter = 0
    for i in range(listLength):
        for j in range(listLength):
            if a[j] > a[j+1]:
                x = a[j]
                a[j] = a[j+1]
                a[j+1] = x
                counter += 1
    print(f'Array is sorted in {counter} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
