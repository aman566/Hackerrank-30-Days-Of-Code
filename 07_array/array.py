#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr1 = []
    for i in range(len(arr)):
        arr1.append(arr[len(arr) - i - 1])
    for i in range(len(arr1)):
        print(arr1[i], end=" ")
