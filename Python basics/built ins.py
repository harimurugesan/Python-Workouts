"""from math import fabs
print(fabs(-9.02))"""

"""a = ['1', '2', '3', '4', '5']
b = ['a', 'b', 'c', 'd', 'e']
print(zip(a, b))
for a, b in zip(a, b):
    print(a)
    print(b)"""
"""num = [22, 3, 2, 55, 6, 2, 0, 47]
char = ['r', 'a', 's', 'z', 'e', 'd']
str = ['hari', 'haaa', 'bala']
dic = {3: "one", 2: "two", 1: "three"}
dicl = [{4: "one", 2: "two", 6: "three"}]

print(sorted(num))
print(sorted(char))
print(sorted(str))
print(sorted(dic))
print(sorted(dicl))

print("\n")

print(sorted(num, reverse=True))
print(sorted(char,  reverse=True))
print(sorted(str,  reverse=True))
print(sorted(dic,  reverse=True))
print(sorted(dicl,  reverse=True))"""

"""def first(text, prefix='e'):
    return text.startswith(prefix)
words = ["hari", "rajee", "sakee", "eliza"]
for i in filter(first, words):
    print(i)"""


"""def first(num):
    return num > 5
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(filter(first, t))
for i in filter(first, t):
    print(i)


def first(t):# if true then takes and stores it in a list else it won't do anything
    return False
t = "hari"
b = "hari"
print(filter(first,t))"""


"""numbers = [11, 22, 3, 4, 56, 76]
print(numbers)


def square(num):

    return num % 2 == 0
print(map(square, numbers))
l = []
for i in numbers:
    l.append(square(i))
print(l)"""

a = [1,2,3,4,5,5]
a.append(4)
print(a)
a.remove(4)
print(a)
print(sorted(a))
print(a.count(4))
a.insert(0,0)
a.insert(1,10)
print(a)
b = (1,2,3)
c = (4,5,6)
print(b + c)
c = {1,2,3,3,3,4,4,8,9,0,0,0,0}
print(c)
c.remove(0)
print(c)
print(set(a))
c.update([11,12,13])
c.add(24)
print(c) 7812836698
