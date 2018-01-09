def ns(n):

    n=5
    print(id(n))

    print(id(mn))
    print("this is mn" ,mn)
    print("this is n",n)
mn=10
print("before  {0}".format(mn))
ns(mn)
print("after {0}".format(mn))



def reassign(list):
  print(id(list))
  list = [0, 1]
  print(list)
  print(id(list))

def append(list):
  list.append(1)

list = [0]
reassign(list)
print(list)
print(id(list))
append(list)
print(list)
print(id(list))


