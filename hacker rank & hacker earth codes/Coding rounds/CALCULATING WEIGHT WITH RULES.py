# a = [12,24]
"""change = 0
for i in a:
    if i % 10 == 0:
        change += 1
    if i % 5 == 0:
        change += 1
    if (i % 4 == 0) and (i % 6 == 0):
        change += 1
print(change)"""
a = []
num = int(input("enter the no of inputs"))
for i in range(1, num+1):
    a.append(int(input("enter the num: ")))

# n = [p for p in range(11) if p > 1]
first = 0
for j in a:
    ps = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
    print("for the input :", j)
    first = 0
    if j in ps:
        first += 5
    if (j % 4 == 0) and (j % 6 == 0):
        first += 4
    if j % 2 == 0:
        first += 3
    print(first)

