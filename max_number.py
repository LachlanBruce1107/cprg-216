a = int(input("Enter Your First Number: "))
b = int(input("Enter Your Second Number: "))
c = int(input("Enter Your Third Number: "))

if (b > a):
    a = b

if (c > a):
    a = c

print("The highest number is ", a)