# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:31:02 2021

@author: Personal
"""

def search(arr, n, x):
 
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
arr = [ 8, 19, 24, 30, 40, 68, 90 ]
x = 30
n = len(arr)
result = search(arr, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)