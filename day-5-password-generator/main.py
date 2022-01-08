import random

letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

list_letters = list(map(chr, range(97, 123)))
list_symbols = list("!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
list_numbers = list(range(1, 10))

password_list = []

for i in range(1, letters_count + 1):
    get_letter = random.choice(list_letters)
    is_Upper = random.randint(0, 1)
    letter = get_letter.upper() if is_Upper else get_letter
    password_list.append(letter)

for i in range(1, symbols_count + 1):
    password_list.append(random.choice(list_symbols))

for i in range(1, numbers_count + 1):
    password_list.append(str(random.choice(list_numbers)))

print(password_list)

random.shuffle(password_list)

print(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")
