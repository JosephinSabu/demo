x=3
y=2.44
z=8+5j
print(type(x))
print(type(y))
print(type(z))
a=float(x)
print(a)
b=int(y)
print(b)
c=complex(x)
print(c)
d=complex(y)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
a="the flowers in the garden are pretty"
print(a)
print(type(a))
print(len(a))
print("are" in a)
print("is" in a)
print("are" not in a)
for i in a:
    print(i)
print(a[1])
print(a[5])
print(a[2:6])
print(a[6:])
print(a[:36])
print(a[-2])
print(a[-30:-5])
print(a.upper())
print(a.lower())
b=" the flowers in the garden are pretty"
print(b)
print(b.strip())
print(b.replace("are","is"))
b=" the flowers, in the, garden ,are pretty"
print(b.split(","))
c="orchid"
print(b+c)
print(f"the {c} flowers in the garden are pretty")
print(b.count("e"))
