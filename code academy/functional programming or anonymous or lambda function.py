

my_list = range(16)

print(filter(lambda x: x % 3 == 0, my_list))  # functional programming only for 2.0x versions

lang = ['python', 'ruby', 'java', 'javascript']
print(filter(lambda x: x = 'python', lang))  # functional programming only for 2.0x versions

squares = [p**2 for p in range(1,11)]
print(filter(lambda x: x>29 and  x<71,squares)) # lambda function usage

