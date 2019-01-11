# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:13:51 2019

@author: Ganesh Patil
"""

num = int(input("Enter a number = "))

if (num > 1):
    for i in range (2,num):
        if(num % i) == 0:
            print(num, "it is not a prime number")
            break
    else:
        print(num, "it is a prime number")
        
else:
    print(num, "it is not a prime number")
