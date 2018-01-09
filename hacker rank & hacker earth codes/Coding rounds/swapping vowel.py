# swapping of vowels
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
