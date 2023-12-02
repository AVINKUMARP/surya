a=[3,8,12,7,6,10,21,15]
c=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if(a[i]+a[j]==18):
            p=(a[i],a[j])
            c.append(p)
print(c)





