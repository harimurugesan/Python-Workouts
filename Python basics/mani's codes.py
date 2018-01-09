l1 = [1,2,3,2,2,2,2,4,4,5,5,3,2,4,5,4,5,5,2,1]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)