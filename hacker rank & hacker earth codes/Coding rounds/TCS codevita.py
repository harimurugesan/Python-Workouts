class Maagic():
    def __init__(self):
        self.s = input()
        self.t = int(input())

    def magic(self):

        self.result = []
        self.Llist = []
        self.Plist= []

        for i in range(self.t):
            self.L1 = input().split()
            self.Llist.append(self.L1[0])
            self.Plist.append(self.L1[1])
        for j in range(self.t):
            self.Lelement = self.Llist[j]
            self.Pelement = self.Plist[j]
            num1 = int(self.Lelement)

            for num in range(len(self.s) - int(self.Lelement) + 1):
                self.v1 = self.s[num:num1]
                if self.v1 not in self.result:
                    if self.s.count(self.v1) == int(self.Pelement):
                        self.result.append(self.v1)
                num1 += 1

        for words in self.result:
            print(words.strip())
obj = Maagic()
obj.magic()

