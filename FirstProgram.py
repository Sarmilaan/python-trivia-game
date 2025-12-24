import math
import os
import random
import re
import sys




t = int(input())
for t_itr in range(t):
    n = int(input())
    add=0
    for i in range (1,n):
        if(i%3==0 or i%5==0):
            add +=i
    print(add)
