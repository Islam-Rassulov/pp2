#Example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Example 2
for x in "banana":
  print(x)

#Example 3 The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Example 4 The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Example 5 The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Example 6
for x in range(6):
  print(x)

#Example 7
for x in range(2, 6):
  print(x)