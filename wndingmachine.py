n=int(input("How many toffee u want?"))
stock=15
i=1
while i<=n:
    if i<=stock:
        print("Collect Toffee=",i)
    else:
        print("out of stock")
        break
    i=i+1
else:  # when the loop runs properly
    print("thank u please visit again")
