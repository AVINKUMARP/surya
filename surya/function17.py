a=[2,3,4,5,6]
b=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if((a[i]*a[j])%2==0) & ((a[i]+a[j])%2==1):
            p=(a[i],a[j])
            b.append()
print(b)