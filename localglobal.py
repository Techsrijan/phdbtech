y=10  # global
x=90
def msg():
    s=globals()['x']  # to access the global variable
    print("Global x=",s)
    global zz
    x=50 #local variable
    zz=55
    print(y)
    print("inside=",x,zz)

print(y)
msg()
print(zz)