a={"door","room","hall"}
print(a)
print(type(a))
print(len(a))
print("door" in a)
print("door" not in a)
for i in a:
    print(i)
a.add("table")
print(a)
b={"brown","green","yellow"}
a.update(b)
print(a)
a.remove("table")
print(a)
a.discard("book")
print(a)
a.discard("hall")
print(a)
a.pop()
print(a)
c=a.union(b)
print(c)
x={"laptop","mobile","tv"}
y={"tv","computer","laptop"}
z=x.intersection(y)
print(z)
z=x.difference(y)
print(z)
z.clear()
print(z)
del z
print(z)