#LINK:-https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461389

from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
start=int(input())
end=int(input())
step=int(input())
for temp in range(start,end+1,step):
    if temp>=0:
        print(str(temp) +"\t"+str(int(((temp-32)*5)/9)))


























