"""i = input().split()
a = [int(p) for p in i]
print(a)
b = [0] * len(i)
b[0] = a[0]
for i in range(1, len(a)):
    sums = 0
    for ii in range(0, i+1):
        sums += a[ii]
    b[i] = sums
print(b)"""

"""t = int(input())
w = input().split()
print(w)
w[0] = int(w[0])
for i in range(t-1):
    w[i + 1] = w[i] + int(w[i+1])
print(w)"""


