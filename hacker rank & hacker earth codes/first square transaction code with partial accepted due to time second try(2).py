i = int(input())
a = input().split()
b = [int(p)for p in a]
num = int(input())
li = []
dic = {}
if len(b) == i:
    for dum in range(num):
        li.append(int(input()))
    for lii in li:
        sums = 0
        lists = []
        if lii <= sum(b):
            if lii not in dic.keys():
                for index, num1 in enumerate(b):
                    sums += num1
                    if sums == lii or sums > lii:
                        lists.append(index + 1)
                print(min(lists))
                dic.update({lii: min(lists)})
            else:
                print(dic[lii])
        else:
            print("-1"