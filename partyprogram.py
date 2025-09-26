print("welcome to the party program")
age = int(input("Please Enter Your Age: "))
gender = input("Please Enter Your Gender, (M/F): ")

if(age >= 18):
    print("Welcome to the party!")
    if(gender == "M"):
        print("You can go to the mens section")
    elif(gender == "F"):
        print("You can go to the womans section")
    else:
        print("uhhhhh, idk where you can go, just hang out I guess")
else:
    print("You're not an adult, you cant come in")