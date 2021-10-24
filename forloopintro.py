from time import *
for i in range(1,10):
    print(i)
    sleep(1)
'''
print()
for i in range(1,10,2):
    print(i,end="")

print()
for i in range(1,11):
    if i%2==0:
        #print(i)
        pass
    else:
        print("odd no=",i)

for k in range(10):
    pass
'''

for i in range(1,11):
    if i%3==0:
        break
    else:
        print(i)

for i in range(1,11):
    if i%3==0:
        continue
    else:
        print(i)