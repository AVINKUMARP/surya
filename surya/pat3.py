a=int(input("enter the limit:"))
k=1
for i in range(0,a):
    for j in range(1,i):
        j=j+j
        print(j,end=" ")
    print()
    