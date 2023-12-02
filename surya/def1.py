class a:
    def my(self):
        print("vegetables")
class b(a):
    def hi(self):
        super().my()
        print("fruits")
class c(b):
    def hlo(self):
        super().hi()
        print("meat")
obj=c()
obj.hlo()