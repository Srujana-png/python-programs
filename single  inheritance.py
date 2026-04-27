class A:
    def one(self):
        print("this is base class")
class B(A):
    def two(self):
        print("this is derived class")
obj=B()
obj.one()
obj.two()



class A:
    def one(self):
        print("this is base class")
class B(A):
    def two(self):
        print("this is derived class")
class c(B):
    def three(self):
        print("this is other class")
obj=c()
obj.one()
obj.two()
obj.three()
