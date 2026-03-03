#Example 1

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Example 2

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)