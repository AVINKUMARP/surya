a=int(input("enter the limit:"))
for i in range(1,a):
    for j in range(0,a):
        print(end=" ")
    a=a-1
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()
    