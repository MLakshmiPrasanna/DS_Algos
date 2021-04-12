# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:55:44 2021

@author: Personal
"""

#QUICKSORT

#divide and conquer algo
#partition process is the key
#we take an element as pivot(mostly first or last elemnt in array) and find 
#exact position of the element. All the elements left of pivot are smaller 
#than pivot not necessarily sorted and elements to the right are greater than pivot
#The we keep calling quicksort recursively on left and right subarrays

###Pseudocode:
    
    #Quicksort(arr[],low,high)
    #{
    #if (low<high)
    #{
    #a=partition(arr[],low,high)
    #Quicksort(arr[],low,a-1)
    #Quicksort(arr[],a+1,high)}}
    
    
def partition(arr,low,high):
    i=low-1
    j=low
    pivot=arr[high]
    for j in range(low,high):
        if(arr[j]<=pivot):
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

arr=[3,2,56,90,23,76,45,62]
n=len(arr)
quicksort(arr,0,n-1)
print(arr)
        
    
    