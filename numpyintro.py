from numpy import *

arr=array([1,2,3,4.0])
print(arr)

for i in arr:
    print(i)

'''
There are six ways to create an array using numpy
1.array()
2.linspace
3.logspace
4.arange
5.zeros
6.ones
'''

a=linspace(1,15,15)
print(a)

print(a[9])

b=logspace(1,50,5)
print(b)

c=arange(15)
print(c)

d=arange(1,15,3)
print(d)

e=ones(20,int)
print(e)

f=zeros(20,int)
print(f)