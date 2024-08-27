a={"name":"nila","age":24,"place":"pathanamthitta"}
print(a)
print(type(a))
print(len(a))
print(a["age"])
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
print("name" in a)
a["name"]="justin"
print(a)
a.update({"place":"kollam"})
print(a)
a["course"]="data analytics"
print(a)
a.update({"duration":"6months"})
print(a)
a.pop("duration")
print(a)
a.popitem()
print(a)
del a["place"]
print(a)
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
b=a.copy()
print(b)
c=dict(b)
print(c)
c.clear()
print(c)
# del c
# print(c)
family={"child1":{"name":"sreya","age":10},"child2":{"name":"gowri","age":16},"child3":{"name":"siya","age":18}}
print(family)
print(family["child2"])
print(family["child2"]["age"])
print(family["child3"]["name"])
