def rec(n):
    if n==0:
        return 1
    else:
        return n*rec(n-1)

n=int(input("enetr any number"))
f=rec(n)
print(f)