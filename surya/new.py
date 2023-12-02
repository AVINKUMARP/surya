a=int(input("enter the limit:"))
i=0
j=0
b=[]
c=[]
d=[]

j=0
while i<=a-1 :
    x=int(input ("enter the num:"))
    b.append(x)
    i=i+1
while j<=len(b)-1:
    if b[j]%2==0:
       c.append(b[j])
       print(c)
    elif b[j]%2!=0:
       d.append(b[j])
       print(d)
    j=j+1
       
       

e=c.extend(d)


print(c)

    
    
    



