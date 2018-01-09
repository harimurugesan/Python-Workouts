a=[p for p in range(51) if p % (3 and 9) == 0] # list comprehension, it is a list created according to some logic
print(a)




a = [int((p * 3)/2)for p in range(1, 11) if p * 3 >= 10] #for p in range(1, 8) ]
print(a)






a = [p**2 for p in range(1, 11) if p % 2 == 0 ]
print(a)



a = ['hari' for i in range(0, 21, 2) if i % 6 == 0 ]
print(a)  # it can be used to have string on list with some conditional numbers





a = [p for p in range(1, 31) if p % 3 == 0]
print(a)
print(a[3:10])
print(a[3:10:2]) # list slicing