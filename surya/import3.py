import re

url = "https://www.washington post.com/news/ww/2016/09/02"

#Check if "Portugal" is in the string:

x = re.findall(r"2016.+02",url)

print(x)