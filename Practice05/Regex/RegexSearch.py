#Example 1

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Example 2
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
