"""
This program generates a random password with three difficulty levels.

The user can choose from three levels:

* Easy: 8 characters, all lowercase letters.
* Medium: 12 characters, lowercase and uppercase letters, and numbers.
* Hard: 16 characters, lowercase and uppercase letters, numbers, and special characters.

The program then generates a random password of the specified difficulty level and prints it to the console.

The user can also enter their own password, and the program will check to make sure that it is at least 4 characters long and no more than 10 characters long.

The program also has a additional features:

1. A password generator that can generate passwords based on specific criteria
"""


import random

easy_alphabet = "abcdefghjkilmnopqrstuvwxyz"
medium_alphabet = easy_alphabet + "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
hard_alphabet = medium_alphabet + "!@#$%^&*()_+?.,"

#Ask user for difficulty level
while True:
    difficulty = input("Enter the diffiuclty level, (easy,medium or hard?)")
    if difficulty in ['easy','medium','hard']:
        # print('Ache bache hu')
        break
    else:
        print('Invalid choice')

#generate random password for each level
if difficulty == 'easy':
    length = 8
    alphabet = easy_alphabet
elif difficulty == 'medium':
    length =10
    alphabet = medium_alphabet
else:
    length =12
    alphabet = hard_alphabet

password = ""
for i in range(length):
    password += random.choice(alphabet)

print("Your Random Password is: ",password)

#Ask for user own password
user_password = input("do you want to enter your own password (y/n)")
if user_password == 'y':
    password = input("Enter you password")
    if len(password) < 4:
        print("Enter the password that is more than 4 characters long ")
    elif len(password) > 10:
        print("Enter the password which is less than 10 characters")
    else:
        print("Password Valid")
else:
    print("Good to see you!")

#Generate password based on user preference

while True:
    Prefernce = input("Do you want to generate password based on your prefernce ")
    if Prefernce in ['y','n']:
        break
    else:
        print('Invalid Input')

if Prefernce == 'y':
    while True:
        CharType = input("Enter your preference (Number, letters or symbols)")
        if CharType in ['letters','numbers','symbols']:
            break
        else:
            print("Invalid Input")

password = ""
for i in range(length):
    password += random.choice(CharType)
print("Your Random Password is: ", password)




