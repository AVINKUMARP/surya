class file():
    def read(self):
        a=str(input("enter file name:"))
        self.f=open(a,"r")
        print(self.f.read())
        self.f.close()
    def create(self):
        a=str(input("enter file name:"))
        self.f=open(a,"x")
        self.f.close()
    def write(self):
        a=str(input("enter text:"))
        file=str(input("enter file name:"))
        self.f=open(file,"a")
        self.f.write(a)
        self.f.close()
obj=file()
while True:
    b=int(input("enter choice:"))    

    if b==1:
        obj.read()
    elif b==2:
        obj.create()
    elif b==3:
        obj.write()
    elif b==4:
        break
    else:
        print("wrong")