import random

def main():
    words = ["python", "wolfram", "hangman", "computer", "science"]
    word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6

    print("=== Hangman ===")

    while attempts > 0:
        # Build the display string showing correct guesses
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display.strip())
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("🎉 You win!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input, try again.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

    else:
        print(f"💀 You lose. The word was '{word}'.")

if __name__ == "__main__":
    main()