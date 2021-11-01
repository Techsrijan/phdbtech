from numpy import *
arr=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
for i in range(3):
    for j in range(3):
        print(arr[i][j],"\t", end="")
    print()

print(arr)

print(arr.dtype)

print(arr.shape)

arr[0][0]=6000
arr[2][2]=6255
print(arr)

print(arr.size)

arr2=arr.flatten()
print(arr2)


arr4=array([
    [1,2,3,4,5,6],
    [2,3,4,5,6,7]
])

print(arr4)
arr5=arr4.reshape(3,4)
print(arr5)

arr6=arr4.reshape((2,2,3))
print(arr6)

arr7=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr+arr7)

d=arr@arr7
print(d)

e=dot(arr,arr7)
print(e)