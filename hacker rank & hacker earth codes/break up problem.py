n = int(input())
w = [0] * 30
for i in range(n):
    msg = input()
    for d in range(30):
        if str(d) in msg.split():
            if 'G:' in msg:
                w[d] += 2
            else:
                w[d] += 1

w19 = w[19]
w20 = w[20]
# print(w19)

flag = 0
if w19 == w20:
    flag = 1;
elif w19 > w20:
    comp = w19
else:
    comp = w20
if flag == 0:
    for d in range(30):
        if d == 19 or d == 20: continue
        if w[d] >= comp:
            flag = 1
            break;

if flag == 0:
    print('Date')
else:
    print('No Date')




4
M: as you wish
M: no way we can go on 21
G:shall we date on 19
G: no 21 only 19
