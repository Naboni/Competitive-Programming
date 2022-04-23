#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    current = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > current:
            arr[i+1] = arr[i]
            print(' '.join(map(str, arr)))
        else:
            arr[i+1] = current
            print(' '.join(map(str, arr)))
            break
    if (arr[0] > current):
        arr[0] = current
        print(' '.join(map(str, arr)))
        
    return arr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
