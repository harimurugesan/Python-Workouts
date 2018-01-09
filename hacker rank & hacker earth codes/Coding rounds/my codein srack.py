aa = int(input())
a =[]
for i in range(aa):
    a.append(input())
one = a[0]
two = a[1]
b =[]
ans =[]
for j in one:
    if j in two:
        b.append(j)
for r in a:
    for r1 in r:
        if r1 not in b:
            if r1 in ans:
                continue
            else:
              ans.append(r1)
print('"'.join(ans))
