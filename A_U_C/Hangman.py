import random

word_list = ["House", "School", "camel", "Techer", "Parent", "Punish"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

hangman = [
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |  /
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-/
 |  /
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-/
 |  / |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-/
 |  / |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-/
 |  / |
 |    |
 |   | |
 |   | |
 |
----------
"""
]

display = ["_" for _ in range(word_length)]
lives = len(hangman) - 1
guessed_letters = []

while "_" in display and lives > 0:
    print(hangman[len(hangman) - 1 - lives])
    print(" ".join(display))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed {guess}.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

if "_" not in display:
    print(hangman[len(hangman) - 1 - lives])
    print(" ".join(display))
    print("You won.")
else:
    print(hangman[-1])
    print(f"The word was: {chosen_word}")
    print("You lost.")
