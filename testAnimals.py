# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:23:23 2022

@author: BENT-ODAI
"""
from animals import Dog  # to import class Dog

resk = Dog(n = 'resk' , col = ['black','white'] ,eyecol = ['blue'],l=40 , w= 50,nation='egy')
lasee = Dog(n = 'lasee' , col=['brown','yellow'],eyecol=['green'],l=30 ,w= 40)
#print ('number of dogs' ,lasee. numOfDogs)

print('resk color',resk.color)
print('resk eye color ',resk.eycolor)
print('resk lemgth',resk .length)
print('resk weight',resk.weight)
resk.run()
resk.set('rayah')
print('lasee color',lasee.color)
print('lasee eye color ',lasee.eycolor)
print('lasee length',lasee .length)
print('lasee weight',lasee.weight)
lasee.run()
lasee.set('ni haw')
