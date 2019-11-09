# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:50:27 2019


This code generates the power of 2 list L(8 terms)
 by 3 different method and calculate the time it
 take in doing so for each method

@author: Ankit Dulat
"""

L=[]
for i in range (0,8):
   L.append(2**i)
   
print(L)
   
import timeit
mycode="""

L=[]
for i in range (0,8):
   L.append(2**i)
"""    
t=timeit.timeit(stmt=mycode,number=1000)
print("Time taken to append the list (2**x inside the loop):",t/1000)


mycode="""
L=[]
def f(n):
    return 2**n
for i in range (0,8):
    L.append(f(i))

"""    
t=timeit.timeit(stmt=mycode,number=1000)
print("Time taken to append the list by defining a function (2**x outdide the loop):",t/1000)


mycode="""
L=[]
g=lambda x:2**x
for i in range (0,8):
    L.append(g(i))

"""    
t=timeit.timeit(stmt=mycode,number=1000)
print("Time taken to append the list using 'lambda'(2**x outdide the loop) :",t/1000)
    
