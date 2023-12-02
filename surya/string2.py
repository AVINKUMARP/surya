a=str(input("enter the string :"))
i=0
count=0
v=("a e i o u")
for i in range(len(a)-1):
    if a[i] in v:
            count+=1
print (count)
