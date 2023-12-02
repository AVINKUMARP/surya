import re

txt = "the quick brown frog jumps over the lazy dog"

#Check if "Portugal" is in the string:

x = re.split("\s",txt)
for i in x:
    if len(i)==3 or len(i)==4:

        print(i)