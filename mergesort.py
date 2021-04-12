# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:30:39 2021

@author: Personal
"""

def merge(a,b):
    c=[]
    a_index,b_index=0,0
    while a_index<len(a) and b_index<len(b):
        if a[a_index]<b[b_index]:
            c.append(a[a_index])
            a_index+=1
        else:
            c.append(b[b_index])
            b_index+=1
    if a_index==len(a):
        c.extend(b[b_index:])
    else:
        c.extend(a[a_index:])
    return c
def mergesort(a):
    if len(a)<=1: return a
    left,right=mergesort(a[:int(len(a)/2)]),mergesort(a[int(len(a)/2):])
    return merge(left,right)

a=[3,2,56,90,23,76,45,62]
print(mergesort(a))
        
            