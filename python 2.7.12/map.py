"""numbers = [1,2,3,4,5]
print(numbers)


def square(num): return pow(num, 2)
print(map(square, numbers))"""


#DIFFERENCE BETWEEN MAP AND FILTER

numbers = [11, 22, 3, 4, 56, 76]
print(numbers)


def square(num):
    
    return num % 2 == 0
print(map(square, numbers))


numbers = [11, 22, 3, 4, 56, 76]
print(numbers)


def square(num):
    
    return num % 2 == 0
print(filter(square, numbers))# filter takes or returns the value when the condition is trrue

#USAGE OF MAP(IT ITERATES THROUGH LIST WITHOUT "for" )
numbers = [11, 22, 3, 4, 56, 76]
print(numbers)


def square(num):
    
    return num-5
print(map(square, numbers))


