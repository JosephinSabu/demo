course=["data analytics","data science","python"]
fees=["10000","12000","15000"]
course[1]="java"
print(course)
course.append("deep learning")
print(course)
course.insert(1,"machine learning")
print(course)
course.extend(fees)
print(course)
course.remove("java")
print(course)
course.pop(1)
print(course)
course.pop()
print(course)
del course[2]
print(course)
location=["pathanamthitta","kollam"]
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)
place=location.copy()
print(place)
area=list(place)
print(area)
kerala=place+location
print(kerala)
print(kerala.count("kollam"))
kerala.clear()
print(kerala)
del kerala
print(kerala)