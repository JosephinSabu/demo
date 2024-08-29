b=(int(input("enter the prime number:")))
if b == 1:
    print("the number is not a prime number")
elif b > 1:
    for i in range(2, b):
        if b % i == 0:
            print("the number is not a prime number")
            break
    else:
        print("the number is prime number")
