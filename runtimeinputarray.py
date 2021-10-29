from array import *
marks=array('i',[]) # empty array

n=int(input("How many elements you want to store"))

for i in range(n):
    x=int(input("Enter the elements of array"))
    marks.append((x))


print(marks)

for i in marks:
    print(i)

search= int(input("Enter the elements u want to search"))

for i in marks:
    if i==search:
        print("item Found")
        break
else:
    print("item not found")

# location finder
for i in range(n):
    if marks[i]==search:
        print("item Found at location=",i+1)
        break
else:
    print("item not found")


# python location finder
print(marks.index(search))