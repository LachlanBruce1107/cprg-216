#Statements we know so far??

#assignment statement

i = 3 #asking to reserve memory of 4 bytes
#and put the value 3 in it
f = 3.4 
msg = "Hello"
message = 'hola'
condition = True
# a variable is a memory that has a size
# a name, an adress, a value, and a type

#Another statement is a fuction call
#The usuage of a function is called a function call

print("Hello World!") #the function takes an argument and print the value of it to the screen
print(3)
print(f)

#lets explore other functions

print(i, type(i))
print(f, type(f))
print(msg, type(msg))
print(condition, type(condition))

#a function call has a name, and ()

input()

def printWelcome():
        print("hello")

printWelcome()

#the casting functions
#implicit casting

x=3
y=4
z=x+y

print("Type of z is ", type(z))
