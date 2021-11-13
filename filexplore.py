'''
f=open("ram4.txt","a")
data=input("enter the text u want to write ")
print(f.write(data))
'''
f2=open("shyam.txt","w")
f=open("ram.txt","r")
#print(f.read())
print("test")
for data in f:
    print(data)
    f2.write(data)

f3=open("test.gif","rb")
f4=open("best.gif","wb")
print(f3)
for data in f3:
    print(data)
    f4.write(data)

