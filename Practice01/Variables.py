#Example 1
x = 5
y = "John"
print(x)
print(y)
#bring type
print(type(x))
print(type(y))


#Example 2
a = 4       # x is of type int
a = "Sally" # x is now of type str
print(a)

#Example 3
b = str(3)    # b will be '3'
c = int(3)    # c will be 3
d = float(3)  # d will be 3.0

#Example 4 Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Example 5 Many Values to Multiple Values
q, w, e = "Orange", "Banana", "Cherry"
print(q)
print(w)
print(e)


#Example Global Variables
r = "awesome"

def myfunc():
  r = "fantastic"
  print("Python is " + r)

myfunc()

print("Python is " + r)


