#Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example 3
print(bool("Hello"))
print(bool(15))

#Example 4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Example 5
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Example 6
x = 200
print(isinstance(x, int))