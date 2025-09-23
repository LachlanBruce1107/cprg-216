condition = True
cond = False

#try to choose a variable name for your boolean expression in the form of a question
is_old = True
has_won = False
is_male = True
is_child = False

expression = 3 > 4

print("Hello to the party program")
user_input = input("Please Enter your age. ")
age = int(user_input)

is_adult = age >= 18

print(is_adult)

user_name = input("What is your name? ")
is_bob = user_name == "bob"
print(is_bob)

x = 23
print(x < 25)
#comparison operators

# equality ==
# larger than >
# larger than or equal >=
# less than <
# less than or equal <=

#example given a, b, c
a = 0
b = 2
c = 4
print((b**2 - 4 * a * c) >= 0)

#if condition :
#    print("yes")

if is_adult:
    print("Yes, is adult") #this line will be ignored if condition is false