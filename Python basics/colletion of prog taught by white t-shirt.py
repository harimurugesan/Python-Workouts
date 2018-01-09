"""def se(li1, li2):
    s = li1[0] == li2[0]
    e = li1[-1] == li2[-1]
    print(s)
    print(e)
    return s and e
print(se([1, 2, 3, 4], [1, 2, 3]))"""


"""a_global = 'global'


def change_global():
    a_global = "local"
    return a_global
print(change_global())
print(a_global) """


"""def add_numbers(a, b, c, *num):   # "*" is used to pass many arguments
    total = 0
    print(a, b, c)
    print(num, type(num))
    for number in num:
        total += number
    print(total)
add_numbers("i am hari", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) """


"""def dic(names):
    for name in names:
        print("the value of {0} is ".format(name), a[name])
a = {"hari": 1, "ravi ": 2, "kavi": 3}
dic(a)
"""

"""l = [1,2,3,4,5,6]
print(l)
l.insert(3,7)

print(l)"""
a= [1,2,3,4]
print(a)
c = a.pop(0)
print(c)
print(a)

