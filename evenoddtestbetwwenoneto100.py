i=1
sum=0
while i<=10:
    if i%2==0:
        sum=sum+i
        print("no is even=",i)
    else:
        print("no is odd=",i)
    i=i+1

print(sum)