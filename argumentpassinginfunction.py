'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument
4. keyword variable length argument
'''

#postional arguments
def person(name,age):
    print(name)
    age=age+10
    print(age)

person('Ram',55)

# keyword argument
person(age=22,name='Mohan')


def add(x,y,z):
    c=x+y+z
    print(c)

add(5,6,6)


#variable length argument
def myadd(x,*y):
    print(x)
    print(y)
    sum=x
    for i in y:
        sum=sum+i
    print(sum)


myadd(44,66,68,5,77,88,8)


def myadd2(*y):
    print(y)
    sum=0
    for i in y:
        sum=sum+i
    print(sum)
myadd2(44,66,68,5,77,88,8)


#keyword variable length argument
def persondata(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

persondata(name='Ram',age=22,city='GKP',mobile=9956485,fname='DASHRATH',pin=273001)
