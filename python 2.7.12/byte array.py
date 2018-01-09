i = int(input())
b = range(1, i+1)
print b
b = list(range(1, i+1))
print b
c = b[::-1]
print c
o = []
for num in range(1, i+1):
    for num1 in c:
        if num1 not in o:
            a = '*'
            sp = ' '
            o.append(num1)
            eval("sp * num1,num * a")
            break
