import random

stages = [
    "X=====X\n |     |\n O     |\n/|\\    |\n/ \\    |\n       |\n=========",
    "X=====X\n |     |\n O     |\n/|\\    |\n/      |\n       |\n=========",
    "X=====X\n |     |\n O     |\n/|\\    |\n       |\n       |\n=========",
    "X=====X\n |     |\n O     |\n/|     |\n       |\n       |\n=========",
    "X=====X\n |     |\n O     |\n |     |\n       |\n       |\n=========",
    "X=====X\n |     |\n O     |\n       |\n       |\n       |\n=========",
    "X=====X\n |     |\n       |\n       |\n       |\n       |\n========="
]

word_list = ["python", "developer", "internship", "hangman", "challenge", "programming"]

def play_game():
    chosen_word = random.choice(word_list)
    guessed_letters = set()
    wrong_guesses = set()
    lives = len(stages) - 1
    word_display = ["_"] * len(chosen_word)

    print("Welcome to Hangman!")
    print("Try to guess the word.\n")

    while lives > 0 and "_" in word_display:
        print(f"Word: {' '.join(word_display)}")
        print(f"Lives left: {lives}")
        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
        print(stages[lives])

        guess = input("Enter a letter (or type 'hint'): ").lower()

        if guess == "hint":
            hidden_letters = [ch for ch, disp in zip(chosen_word, word_display) if disp == "_"]
            if hidden_letters:
                hint_letter = random.choice(hidden_letters)
                print("Hint: The word contains '" + hint_letter + "'")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("You already tried '" + guess + "'")
            continue

        if guess in chosen_word:
            print("Good job! '" + guess + "' is in the word.")
            for i, ch in enumerate(chosen_word):
                if ch == guess:
                    word_display[i] = ch
            guessed_letters.add(guess)
        else:
            print("'" + guess + "' is not in the word.")
            lives -= 1
            wrong_guesses.add(guess)

    if "_" not in word_display:
        print("\nYou guessed the word: " + chosen_word + "! YOU WIN!")
    else:
        print(stages[0])
        print("\nGame Over! The word was: " + chosen_word)

while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye.")
        break
