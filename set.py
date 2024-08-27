a={"apple","banana","mango"}
print(a)
print(type(a))
print(len(a))
print("mango" in a)
print("mango" not in a)
for i in a:
    print(i)
a.add("grape")
print(a)
b={"rose","orchid","jasmine"}
a.update(b)
print(a)
a.remove("grape")
print(a)
a.discard("strawberry")
print(a)
a.discard("mango")
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