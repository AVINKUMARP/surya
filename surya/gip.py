a=int(input("enter the limit:"))
i=0
j=0
b=[]
c=[]
while i<=a-1 :
    x=str(input("enter the string"))
    b.append(x)
    i=i+1
while j<=len(b)-1:
        c.append(b[j].capitalize())
        j+=1
        
print(c)
        
