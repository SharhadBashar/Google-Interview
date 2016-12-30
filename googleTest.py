#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 01:44:53 2016
@author: Sharhad Bashar
"""
def roundUp(num):
    if (num % 2 == 0):
        return num / 2
    else:
        return (num / 2 + 1)

def numGen (X):
    orgNum = X
    orgLen = len(str(X))
    length = len(str(X))
    avg = 0
    finalVal = 0
    brokenNum = [0 for i in range (length)]#creates the array
    a = [[0 for i in range (length - 1)] for i in range (length - 1)]
    finalNum = [0 for i in range (length - 1)]     
    while (X > 0):
        brokenNum[length - 1] = X % 10
        X = X/10
        length -= 1

    for i in range (orgLen - 2):
        avg = (brokenNum[i] + brokenNum[i+1])
        a[i][i] = roundUp(avg)
        
    a[length - 1][length - 1] = roundUp((brokenNum[orgLen - 2] + brokenNum[orgLen - 1]))
    #at this point, all the averages are in the right place

    for i in range (orgLen - 1):
        for j in range (orgLen - 1):
            if (a[i][j] == 0):
                if (i < j):
                    a[i][j] = brokenNum[j + 1]
                elif (i > j):
                    a[i][j] = brokenNum[j]
                    
    for i in range (orgLen - 1):
        sum = 0
        for j in range (orgLen - 1):
            sum += a[i][j]*pow(10,orgLen - 2 - j)
            finalNum[i] = sum
    
    for i in range (orgLen - 1):
        if (finalNum[i] > finalVal):
            finalVal = finalNum[i]
    
    return finalVal
    
X = 623315   
a = numGen (X)
print a
