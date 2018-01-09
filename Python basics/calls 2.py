def pr(l):
    print(id(list))
    print(id(l))
    l=[1,2,3]
    print(l)
    print(list)
    print(id(l))

list=[7,8,0]
print("before ",list)
pr(list)
print("after",list)