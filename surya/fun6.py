def sq(a):
    b=[]
    i=0
    c=[]
       
    for i in range (0,a):
            x=int(input("enter the num:"))
            b.append(x)
            print(b)
            if i<=a:
                c=b[i]**2
            print(c)
a=int(input("enter the limit:"))
sq(a)