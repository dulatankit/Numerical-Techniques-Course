# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:30:34 2019

@author: Ankit Dulat
"""
S='mumbai' 

# comprehension method
d=[(i,ord(i)) for i in S]
print(list(d))
unicod1=[ ord(i) for i in S ]
t=sum(list(unicod1))
print("Sum of unicode points of all letters of mumbai is:",t)
print("The list that contain the Unicode points by COMPREHENSION:",list(unicod1))


# map method
unicod2=list(map(lambda x: ord(x),S))
print("The list that contain the Unicode points by using MAP:",list(unicod2))

L=[]
for i in S:
    m = ord(i)
    L.append(m)
print("The list that contain the Unicode points by using LIST is:",L)