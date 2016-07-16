#!/usr/bin/env python
# coding=utf-8

#这是一个简单的python冒泡排序

array = [1,2,5,3,6,8,4]

for i in range(len(array)-1,0,-1):
    for j in range(0,i):
        if array[j]>array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]

print array