i = int(input())
a = input().split()
b = [int(p)for p in a]
num = int(input())
li = []
if len(b) == i:
    for dum in range(num):
        li.append(int(input()))
    for lii in li:
        sums = 0
        lists = []
        if lii <= sum(b):
            for index, num1 in enumerate(b):
                sums += num1
                if sums == lii or sums > lii:
                    lists.append(index + 1)
            print(min(lists))
        else:
            print("-1")