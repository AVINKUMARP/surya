import re

s = "abd abcd abccd abcccd abed"

#Check if "Portugal" is in the string:

x = re.findall(r'ab.*cd',s)

print(x)