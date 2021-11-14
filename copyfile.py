f=open("ram.txt","r")
f2=open("mohan.txt","w")
for data in f:
    #print(data)
    f2.write(data)
f.close()

for data in f2:
    print(data)
f2.close()
'''
f3=open("mohan.txt","r")
for data in f3:
    print(data)
'''