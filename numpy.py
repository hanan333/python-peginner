# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 23:18:49 2022

@author: BENT-ODAI
"""

import numpy as np
num=[4,5,6,7,8]
print (type(num))
numvec=np.array(num)
print (type(numvec))
numList=[[2,3],[4.5]]
print (type(numList))
numMatrix=np.array(numList)
print (type(numMatrix))

print (len(num))
print(len(numvec))
print(numMatrix.size)
list(range(0,10))
x = np.arange(0,27,3)##creat automatic vector
n1 ,n2 = np.mgrid[3:5 , 2:7]  ##creat automatic vector
z=np.zeros(6)
z1=np.ones(6)
zeromat = np.zeros((6,3))
onemat = np.zeros((6,3))
x3=np.arange(0,10,0.1)
y = np.linspace(0,10,25) #according to numberof samples
r2 = np.random.rand(5,3)##unform distrbution from zero to one
rn=np.random.randn(5,4) ##from -1
i=np.eye(5)##diagonal=1