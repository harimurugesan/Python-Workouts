i = int(input())
a = []
for ii in range(i):
    a.append(int(input()))
for aa in a:
    if aa % 21 == 0 or '21' in str(aa):
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")