#Example 1

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Example 2

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)