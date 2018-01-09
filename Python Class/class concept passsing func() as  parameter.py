class b():
    def __init__(self,cw,pk):
        self.cw=cw
        self.pk=pk
        print(self.cw)
        print(self.pk)
    def change(hari):
        print("the name is {0}" .format( hari.cw))

    def range(self,text):
        self.text=text
        print(self.text)

    def mathop(self,mathcalc,*args):
        print("{0} performed mathcalc and the result is {1}".format(self.cw,mathcalc(*args)))
def add(a,b):
    return a+b

hari=b("hari","male")
hari.mathop(add,20,30)# we passed add function()as argument
