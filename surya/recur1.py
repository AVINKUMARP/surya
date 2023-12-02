def num(n):
    if n>=0:
        a=n
        print(a)
        n=num(n-1)
    return(a)
b=int(input("enter number:"))
r=num(b)
print(r)