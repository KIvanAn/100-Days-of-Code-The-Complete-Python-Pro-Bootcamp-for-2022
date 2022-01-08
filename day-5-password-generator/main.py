import random

letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

list_letters = list(map(chr, range(97, 123)))
list_symbols = list("!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
list_numbers = list(range(1, 10))

password = []

for i in range(1, letters_count + 1):
    get_letter = random.choices(list_letters)[0]
    is_Upper = random.randint(0, 1)
    letter = get_letter.upper() if is_Upper else get_letter
    password.append(letter)

for i in range(1, symbols_count + 1):
    symbol = random.choices(list_symbols)[0]
    password.append(symbol)

for i in range(1, numbers_count + 1):
    number = random.choices(list_numbers)[0]
    password.append(str(number))

print(password)

random.shuffle(password)

print(password)

str_password = "".join(password)

print(f"Your password is: {str_password}")
