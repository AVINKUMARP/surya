a=int(input("enter the limit :"))
for i in range(a,-1,-1):
    for j in range(i+1):
        if j==0 or j==i or i==a:
            print("*" ,end=" ")
        else:
         print(" ",end=" ")
    print()