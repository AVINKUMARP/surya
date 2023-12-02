class Account:
    def __init__(self,name,num,bal):
        self.name=name
        self.num=num
        self.bal=bal
    def withdrow(self):
        n=int(input("enter the amt to withdrow: "))
        self.bal=self.bal-n
    def deposit(self):
        n=int(input("enter the amt to deposit: "))
        self.bal=self.bal+n
    def show(self):
        print(self.bal)
l=[]
while True:
    n=int(input("enter choice:"))
    if n==1:
        name=str(input("enter user name: "))
        num=int(input("enter user id: "))
            
        bal=int(input("enter balance: "))
        x=Account(name,num,bal)
        l.append(x)
    if n==2:
        accno=int(input("enter accno: "))
        for i in l:
            if i.num==accno:
                i.deposit()
            else:
                print("no such AC") 
    if n==3:
        accno=int(input("enter accno: "))
        for i in l:
            if i.num==accno:
                i.withdrow()
            else:
                print("no such AC") 
    if n==4:
        accno=int(input("enter accno: "))
        for i in l:
            if i.num==accno:
                i.show()
            else:
                print("no such AC") 
    if n==5:
        print("Exit")
        break