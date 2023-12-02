import re
data=("^([012]\d|3[01])-([0]\d|1[012])-(\d{4})")
if re.search(data,"18-11-2001"):
    print("match")
else:
    print("not match")
    
 