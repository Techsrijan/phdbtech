from numpy import *
arr=array([1,2,3,4,5])
print(arr,"id of arr=",id(arr))
arr2=arr  #alisaing
print(arr2,"id of arr2=",id(arr2))

arr[1]=5000
print(arr,"id of arr=",id(arr))

print(arr2,"id of arr2=",id(arr2))

# what if u want two different array

arr3=array([1,2,3,4,5])
arr4=arr3.view()   #shallow copy
print(arr3,"id of arr3=",id(arr3))
print(arr4,"id of arr4=",id(arr4))

arr3[0]=2000
print(arr3,"id of arr3=",id(arr3))
print(arr4,"id of arr4=",id(arr4))

#what if u want two different array  and change of one does not affect
#other
arr5=array([1,2,3,4,5])
arr6=arr5.copy()  #deep copy
print(arr5,"id of arr5=",id(arr5))
print(arr6,"id of arr6=",id(arr6))

arr5[0]=1000
print(arr5,"id of arr5=",id(arr5))
print(arr6,"id of arr6=",id(arr6))

