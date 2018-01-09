i = input().split()
a = [int(i[0])]
b = [int(i[1])]
for ii in i:
    if ii == i[0]:
        if '5' or '6' in ii:
            for index, num in enumerate(ii):
                if '5' in num:
                    new = list(ii)
                    new[index] = '6'
                    a.append("".join(new))
                if '6' in num:
                    new = list(ii)
                    new[index] = '5'
                    a.append("".join(new))
    if ii == i[1]:
        if '5' or '6' in ii:
            for index, num in enumerate(ii):
                if '5' in num:
                    new = list(ii)
                    new[index] = '6'
                    b.append("".join(new))
                if '6' in num:
                    new = list(ii)
                    new[index] = '5'
                    b.append("".join(new))
if '5' in i[0]:
    a.append(i[0].replace('5', '6'))
if '6' in i[0]:
    a.append(i[0].replace('6', '5'))
if '5' in i[1]:
    b.append(i[1].replace('5', '6'))
if '6' in i[1]:
    b.append(i[1].replace('6', '5'))
newly = []
newly2 = []
for inch in a:
    newly.append(int(inch))
for inch1 in b:
    newly2.append(int(inch1))
print((min(newly) + min(newly2)) ,(max(newly) + max(newly2)))




