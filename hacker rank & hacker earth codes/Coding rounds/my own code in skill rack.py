a = input()
count = 0
cc = len(a)
c = int(a)
#pp = a.count('0')
pc = 0
for i in a:
    b = int(i)
    if b == 0:
        pc+=1
        continue
    if c % b == 0:
        count += 1
    else:
        pc += 1
        co = 0
if count > 0:
    print(count)
if pc == cc:

    print(co)
