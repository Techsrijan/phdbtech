from array import *

marks=array('f',[1,2,3,5,6.0])

print(marks)

print(marks[0],marks[-1],len(marks))
for i in marks:
    print(i)

for i in range(len(marks)):
    print(i,"=",marks[i])

