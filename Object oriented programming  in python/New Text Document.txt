class SuperClass:
    def __init__(self,a,b):

        self.a = a
        self.b = b


class BaseClass1(SuperClass):
    def base1(self):
        print(self.a * self.b)


class BaseClass2(BaseClass1):
    def __init__(self,a,b,c):
        super(BaseClass2,self).__init__(a,b)
        self.c = c

    def base2(self):
        print(self.a + self.b + self.c)

b1 = BaseClass1(10,20)
b1.base1()
b2 = BaseClass2(10,20,10)
b2.base2()