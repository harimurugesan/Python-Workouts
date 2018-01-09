in1 = input().split()
x = in1[0]
y = in1[1]
sums = int(x) + int(y)
flag = 0
a = []
b = []
if '5' or '6' in x:
    flag += 1
    if '5' in x:
        for index,num in enumerate(x):
            if num == '5':
                a.append(index)
                x = x.replace('5', '6')
    if '6' in x:
        for index,num1 in enumerate(x):
            if num1 == '6':
                if index not in a:
                    x = list(x)
                    x[index] = '5'
                    x = "".join(x)

if '5' or '6' in y:
    flag += 1
    if '5' in y:
        for index, num in enumerate(y):
            if num == '5':
                b.append(index)
                y = y.replace('5', '6')
    if '6' in y:
        for index, num1 in enumerate(y):
            if num1 == '6':
                if index not in b:
                    y = list(y)
                    y[index] = '5'
                    y = "".join(y)

if flag == 0:
    print(sums)
else:
    newly = int(x) + int(y)
    print(min(sums, newly) ,max(sums, newly))

