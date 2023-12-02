# y=[]
# b=[]
# x=[4,8,7,3]
# a=[5,9,1,2]
# for i in range(0,len(x)):
#     for j in range(0,len(x)):
#         if x[i]+x[j]==10:
#             z=(x[i],x[j])
#             k=i
#             y.append(k)
# for i in range(1,len(a)):
#     for j in range(0,len(a)):
#         if a[i]+a[j]==10:
#             w=(a[i],a[j])
#             k=i
#             b.append(k)
# print(y)
# print(b)
 
 
r=[4,8,7,3,4,1] 
s=[5,9,1,2,3,6]
t=[]
v=[]
for i in range(0,len(r)):
    for j in range(0,len(r)):
        if r[i]+s[j]==10:
            x=i
            n=j
            t=x
            v=n
            print("r:",t)
            print("s:",v)
               