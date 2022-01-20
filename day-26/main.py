import pandas


data = pandas.read_csv("data/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}

word = input("Enter a word: ").upper()

result = [phonetic_dict[letter] for letter in word]

print(result)

