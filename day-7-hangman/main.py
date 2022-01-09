import random

from hangman_art import logo, stages
from hangman_words import word_list


finish_game = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display_word = ["_" for _ in range(word_length)]

print(logo)

while not finish_game:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in display_word:
        print(f"You've already guessed {guess_letter}")

    for idx in range(word_length):
        if chosen_word[idx] == guess_letter:
            display_word[idx] = guess_letter

    print(" ".join(display_word))

    if guess_letter not in chosen_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            finish_game = True
            print("You lose.")

    if "_" not in display_word:
        finish_game = True
        print("You win.")

    print(stages[lives])
