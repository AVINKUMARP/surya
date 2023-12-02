import re

s = "cat mat pat sat rat"

#Check if "Portugal" is in the string:

x = re.findall(r'[cpr]at',s)

print(x)