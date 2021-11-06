from functools import *
def add(x,y):
    return x+y

print(add(5,6))

f=lambda a,b:a+b

res=f(55,60)
print(res)

ls=[1,2,3,4,5,6,7,8,9,10]

is_even=lambda n:n%2==0

op=list(filter(is_even,ls))
print(op)

mymap=lambda n:n+10
op2=list(map(mymap,op))
print(op2)

red=lambda p,q:p+q
s=reduce(red,op2)
print(s)