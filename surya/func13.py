def sq(a):
    b=[]
    i=0
    d=[]
       
    for i in range (0,a):
            x=int(input("enter the num:"))
            b.append(x)
            
            if i<=a:
                c=b[i]**2
                d.append(c)
                if i<=a:
                    Sum=sum(d)
                    
                print(b)
                print(c)
                print("sum of list:",Sum)
a=int(input("enter the limit:"))
sq(a)