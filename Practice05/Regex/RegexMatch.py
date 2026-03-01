#Example 1

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#Example 2

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Example 3

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Example 4

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
