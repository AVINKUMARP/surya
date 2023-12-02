a=['apple', 'banana', 'cherry', 'date']
b=[]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        for char in a[i]:
            if char in a[j]:
                p=(a[i],a[j])
                b.append(p)
                break
print(b)