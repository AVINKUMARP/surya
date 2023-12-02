class Bank:
    def __init__(self):
        self.num=123
        self.name="john"
        self.bal=10000
    def withdrow(self):
        n=int(input("enter the amt to withdrow: "))
        self.bal=self.bal-n
    def deposit(self):
        n=int(input("enter the amt to deposit: "))
        self.bal=self.bal+n
    def show(self):
        print(self.bal) 
o=Bank()
while True:
        m=int(input("enter choice:"))
        if m==1:
            o.deposit()
        elif m==2:
            o.withdrow()
        elif m==3:
            o.show()
        elif m==4:
            print("Exit")
            break
        else:
            print("wrong choice")