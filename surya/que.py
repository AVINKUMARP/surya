a=str(input("enter the word:"))


i=0
n=len(a)
d={}



while i<n:
    s=a[i]
    if s in d:
        d[s]+=1
    else:
        d[s]=1
    i=i+1
print(d)
        