def fact(n):
    if n==1:
       f=1
    else:
        f=n*fact(n-1)
    return f
num=int(input("enter the number"))
result=fact(num)
print(result)