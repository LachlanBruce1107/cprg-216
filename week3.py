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


def printWelcome():
        print("hello")

printWelcome()

#the casting functions
#implicit casting

x=3
y=4
z=x+y

print("Type of z is ", type(z))

#operators

# + - / *
x = 3+4
y = 3 * 4
z = 3/4

#the remainder %

v = 4%3 # 1
x = 5//3 #1 floor division, rounds to lower
y = 2**3 #power, 2*2*2

print(v, x, y)

# augmented operators

x = x + 3 # 4
print(x)
#a shorthand for that
x += 3 #this is equivalent to x = x+3
y *= 2
print(x)
print(y)
y /= 8
print(y)

#when we try to write something that is large
#we go to the next line

'''
Now I can use this kind of commenting
to comment several lines
it is good for documentation
'''

#print function in detail

print("hello", "world", "Hey")
print("hello", x+y )