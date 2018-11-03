#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    dictionary = {}
    for i in range(6):
        x = input()
        y = []
        y = x.split(' ')
        dictionary.update({i:y})
    new_array = []
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += int(dictionary[i][j])+int(dictionary[i][j+1])+int(dictionary[i][j+2])
            sum += int(dictionary[i+1][j+1])
            sum += int(dictionary[i+2][j])+int(dictionary[i+2][j+1])+int(dictionary[i+2][j+2])
            new_array.append(sum)
            sum=0
    print(max(new_array))
