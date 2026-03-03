#Example 1
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Example 2

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

