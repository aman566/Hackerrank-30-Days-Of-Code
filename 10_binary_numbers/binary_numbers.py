#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    if n==0:
        print(0)
        exit()
    x = list()
    while(n!=0):
        x.append(n%2)
        n=n//2
    
    count = 1
    new_list = []
    for i in range(len(x)-1):
        if x[i] == 1 and x[i] == x[i+1]:
            count += 1
        else:
            new_list.append(count)
            count = 1
    new_list.append(count)        
    print(max(new_list))
