a=int(input("enter the limit:"))
p=-1
for i in range(0,a):
    for j in range(0,i+1):
        p+=1
        print(chr(65+p),end=" ")
    print()
    