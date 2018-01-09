def i_return(x):
    print (x)
    return (x)

def i_dont(x):
    print (x)

a=i_return(8)
print("returned value is ", a)# prints 5
i_dont(5)
print (i_return(8) + 2)    # prints 7
