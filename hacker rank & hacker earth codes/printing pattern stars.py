i = int(input())
b = list(range(1, i+1))
c = b[::-1]
o = []
o1 = []
for num in b:
    for num1 in c:
        if num1 not in o:
            a = '*'
            sp = ' '
            o.append(num1)
            print(sp * num1,num * a)
            break
for num in c:
    for num1 in b:
        if num1 not in o1:
            a = '*'
            sp = ' '
            o1.append(num1)
            print(sp * num1,num * a)
            break
