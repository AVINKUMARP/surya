i =2
n=1 #used for counting

while 10>=n:
        for j in range(1,i):
            x =1
            while x*x<=j:
                if x*x==j:
                    print(j)
                    n+=1
                x+=1
            i+=1
            j+=1
            