class A:
    x=int(input("enter integer1"))
    y=int(input("enter integer2"))
    z=input("enter string")
    def a(self,a,b):
        print("reverse of string2",a[::-1])
        print("square of integer3",b*b)
    def displayresults(self):
        print("length of string",len(self.z))
        print("modulus",self.x%self.y)
x=input("enter string 2")
y=int(input("enter integer3"))
obj=A()
obj.a(x,y)
obj.displayresults()
