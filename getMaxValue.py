import math
import os
import random
import re
import sys

def getMaxValue(arr):
  arr.sort()
  current=1
  for i in range(1,len(arr)):
    if arr[i]>=current+1:
      current+=1
  return current
if __name__=='__main__':
  fptr=open(os.environ['OUTPUT_PATH'],'W')
  arr_count=int(input().strip())
  arr=[]
  for _ in range(arr_count):
    arr_item=int(input().strip())
    arr.append(arr_item)
  result=getMaxValue(arr)
  fptr.write(str(result)+'\n')
  fptr.close()




#other formate 


import os

def getMaxValue(arr):
    arr.sort()
    current = 1

    for num in arr:
        if num <= current:
            current += num
        else:
            break

    return current


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'W')

    arr_count = int(input().strip())
    arr = []

    for _ in range(arr_count):
        arr.append(int(input().strip()))

    result = getMaxValue(arr)

    fptr.write(str(result) + '\n')
    fptr.close()


















