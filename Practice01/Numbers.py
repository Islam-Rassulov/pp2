#Example 1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Example 2
q = 1    # int
w = 2.8  # float
e = 1j   # complex

#convert from int to float:
a = float(q)

#convert from float to int:
b = int(w)

#convert from int to complex:
c = complex(q)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Example 3 Random Number
import random

print(random.randrange(1, 10))