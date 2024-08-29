#sum of 1st 10 natural numbers
sum=0
for i in range(1,11):
    sum+=i
print(sum)
#factorial of a number
n=6
h=1
for i in range(1,n+1):
    h*=i
print(h)
#sum of even number
a=0
for i in range(1,21):
    if i %2==0:
        a+=i
print(a)
#sum of square of 1st 10 numbers
b=0
for i in range(1,11):
    b+=i**2
print(b)
#fibonacci series
number=8
a,b=0,1
count=0
print(a,end='')
for i in range (1,number):
    print(b,end='')
    c=a+b
    a=b
    b=c
#average of three numbers
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
sum=0
sum=a+b+c
avg=sum/3
print(avg)
#prime or not
x=int(input("enter the prime number"))
if x==1:
    print("the number is not a prime number")
elif x>1:
    for i in range (2,x):
          print("the number is not a prime number")
          break
    else:
        print("the number is prime number")


