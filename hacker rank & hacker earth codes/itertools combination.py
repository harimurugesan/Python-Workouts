from itertools import combinations
i = input().split()
a = i[0]
b = int(i[1])
for ii in range(1,b+1):
    d =[]
    c = list((combinations(a,ii)))
    for cc in c:
        d.append(sorted(cc))
    d = list(sorted(d))
    for re in d:
        print("".join(re))






Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK







