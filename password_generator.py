#This was a coding challenge with my brother, that's the reason for using beginner concepts only.
# in the hard Version it would have been easier to generate a password withg the easy version then use random.shuffle()

import  random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_len = nr_numbers + nr_letters + nr_symbols
password=""

#easy Version
# for letter_nr in range(nr_letters):
#     password += random.choice(letters)
# for symbol_nr in range(nr_symbols):
#     password += random.choice(symbols)
# for number_nr in range(nr_numbers):
#     password += random.choice(numbers)

#harder version
all_characters = [letters,numbers,symbols]
still_to_use=[]
if nr_letters > 0:
    still_to_use.append(0)
if nr_numbers > 0:
    still_to_use.append(1)
if nr_symbols > 0:
    still_to_use.append(2)

for i in range(password_len):
    choose_from = random.choice(still_to_use)
    if choose_from == 0:
        password += random.choice(letters)
        nr_letters -= 1
        if nr_letters == 0:
            still_to_use.remove(0)
    if choose_from == 1:
        password += random.choice(numbers)
        nr_numbers -= 1
        if nr_numbers == 0:
            still_to_use.remove(1)
    if choose_from == 2:
        password += random.choice(symbols)
        nr_symbols -= 1
        if nr_symbols == 0:
            still_to_use.remove(2)





print(password)
