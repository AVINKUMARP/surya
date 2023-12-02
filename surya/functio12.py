a=int(input("enter the limit :"))
for i in range(1,a+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
    if i%2==0:
        for j in range(1,i+1):
            print(j,end=" ")
    else:
        for k in range(i,0,-1):
            print(k,end=" ")
    print()
       
    
                    


                    
                    
                    
               