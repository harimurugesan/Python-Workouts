def func1(list):
     print (list)
     list += [47,11]
     print (list)

fib = [0,1,1,2,3,5,8]
func1(fib)

print (fib)

# shallow copying done for preventing variable change
def func1(list):
    print(list)
    list += [47, 11]
    print(list)


fib = [0, 1, 1, 2, 3, 5, 8]
func1(fib[:])

print(fib)


# another method of passing a copy to the function
def func1(list):
    print(id(fib))
    print(id(list))
    print(list)
    a=[list]
    a+= [47, 11]
    print(a)
    print(list)
    print(id(list))

fib = [0, 1, 1, 2, 3, 5, 8]
func1(fib)

print(fib)




