x={"name":"kavya","age":22,"course":"python"}
print(x)
print(type(x))
print(len(x))
print(x["course"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
print("name" in x)
x["name"]="parvathi"
print(x)
x.update({"course":"data analytics"})
print(x)
x["age"]="25"
print(x)
x.update({"duration":"6months"})
print(x)
x.pop("duration")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
x["age"]=24
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
y=x.copy()
print(y)
z=dict(y)
z.clear()
print(z)
classmates={"friend1":{"name":"gowri","gender":"female"},"friend2":{"name":"joel","gender":"male"}}
print(classmates)
print(classmates["friend1"])
print(classmates["friend2"]["gender"])
print(classmates["friend1"]["name"])
