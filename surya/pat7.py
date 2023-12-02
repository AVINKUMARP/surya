a=int(input("enter the limit :"))
p=chr
for i in range(a):
    print(chr(65+i),end=" ")
    for j in range(1,i+1):
        p=chr(65+i-j)
        print(p,end=" ")
    print()

