d={1,2,3,5,5,4,33}
print(d)
print(type(d))

s=set()
print(type(s))

a={1,2,8,6,7}

#union
print(a|d)

#intersection

print(a&d)

#difference
print(a-d)
print(d-a)

#symmetric difference

print(a^d) #not common in intersection

c=set()
c=a.copy()
print(c)

print(c.clear())