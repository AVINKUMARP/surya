n=int(input("enter the limit"))
for i in range(n):
    for j in range(n,i+1,-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        elif i==2 or i==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()