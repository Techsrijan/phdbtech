def greet():
    print("Good Morning")

greet()
greet()

'''
def add():
    a,b=5,9
    c=a+b
    print(c)
    
add()    
'''

def add(x,y):
    c=x+y
    print("Sum=",c)

add(3,5)

p=int(input("enter first number"))
q=int(input("enter second number"))
add(p,q)

# return statement
def calci(x,y):
    c=x+y
    m=x*y
    return c

greet()
'''
result,result1=calci(4,5)
print("this is the sum of two no=",result)
print("this is the multiplication of two no=",result1)
'''
d=2+calci(4,5)
print(d)