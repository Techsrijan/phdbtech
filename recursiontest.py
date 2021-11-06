import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(sys.getrecursionlimit()-200)
i=1
def msg():
    global  i
    print("Good morning",i)
    i=i+1
    msg()


# when a function calls iteself it is called recursion
msg()