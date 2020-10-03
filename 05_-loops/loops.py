#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = eval(input())
    for i in range(1,11):
        print(str(n)+" x "+str(i)+" = "+str(n*i))
    i = 0
    while(i < 5):
        print(str(n)+" x "+str(i)+" = "+str(n*i))
