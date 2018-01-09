class enemy:
    def __init__(self,x,y):
        self.power=x
        self.capsule=y

    def health(self,r,j):
        self.rome=r
        self.jack=j
        print(self.rome)
        print(self.jack)
        print(self.power)
        print(self.capsule)
v=enemy(8,9)
v.health(5,5)


