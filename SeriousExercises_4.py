num = int(input("Enter your number :"))
if num < 0:
    print("Re-enter please !")
elif num % 2 == 0:
    print(num, " is not a prime number")
elif num % 3 == 0:
    print(num, " is not a prime number")
else :
    print(num, " is a prime number")