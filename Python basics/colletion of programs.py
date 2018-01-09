"""# swapping of vowels
import random
vowels = ['a', 'e', 'i', 'o', 'u']
message = input("enter the string: ")
new_message = ""
for letter in message:
    if letter not in vowels:
        new_message += letter
    if letter in vowels:
        temp = random.choice(vowels)
        while temp != letter:
            temp = random.choice(vowels)
        new_message += temp
print(new_message)
"""

# print(*range(1, int(input())+1), sep='  ')
# print(pow(10.2,2))
# print(int("956"))

"""a = input()
b = input()
m = int(input())
if '.' in a:
    a = float(a)
else:
    a = int(a)
if '.' in b:
    b = float(b)
else:
    b = int(b)
print(pow(a, b))
print(pow(a, b, m)"""


L = []
for _ in range(0, int(input())):
    user_input = input().split(' ')
    command = user_input.pop(0)
    if len(user_input) > 0:
        if 'insert' == command:
            eval("L.{0}({1}, {2})".format(command, user_input[0], user_input[1]))
        else:
            eval("L.{0}({1})".format(command, user_input[0]))
    elif command == 'print':
        print(L)
    else:
        eval("L.{0}()".format(command))

