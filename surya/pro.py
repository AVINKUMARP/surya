a=int(input("enter the number of days"))
d={31: "january, march, may, july, august, october, and december",28: "february", 30: "april, june, september, november"}
print("The months with",a,"days are :",d[a]) 
n= input("enter month:")
if (n in d[30]):
    print("30 days")
elif(n in d[31]):
    print("31 days")
else:
    print("28 days ")