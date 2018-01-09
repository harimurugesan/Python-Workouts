class b():
    def __init__(self):
        self.cw=20
        self.pk=100
def change(hari):
    hari.cw=40
    hari.pk=777
b=b()
print(b.cw)
print(b.pk)
change(b)
print(b.cw)
print(b.pk)