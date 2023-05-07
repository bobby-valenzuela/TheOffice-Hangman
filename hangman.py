import random
from hangman_art import logo, stages
from replit import clear

word_list = [
    "Bigboobz", "chumbo", 
    "stanley is having an affair",
    "That's what she said", 
    "I am Beyonce, always",
    "Sorry I annoyed you with my friendship", 
    "I'm a little stitious",
    "why waste time say lot word, when few word do trick?",
    "Dwight, you ignorant slut",
    "Who is Justice Beaver?",
    "Why are you the way that you are?"
]

chosen_word = random.choice(word_list)

print(logo)

# Create Letters to display
display = []

for c in chosen_word:
    if c in [' ', ',', "'", '?']:
        display += c
    else:
        display += "_"

# print(chosen_word)

lives_left = 6
game_over = False
incorrect_guesses = []

while not game_over:

    # print(f"\n\n=== Lives left {lives_left}/6 ===")

    # Print ASCII art if any failed guesses
    if lives_left < 6 and not game_over:
        print(stages[lives_left])

        # Print incorrect guesses  
        print(f"Incorrect Guesses: {','.join(incorrect_guesses)}\n")
  
    formatted_display = [l + " " for l in display]
    print("\n" + "".join(formatted_display))
  
    guess = input("\n\nGuess a letter: ").lower()

    # Skip identical guesses
    if guess in display or guess in incorrect_guesses:
        clear()
        print(f"You already guessed: {guess}. Try again.")
        continue

    # Reduce tries if no match
    if guess not in chosen_word.lower():
        lives_left -= 1
        clear()
        print(f"{guess} is incorrect. You lose a life!")
        incorrect_guesses += guess
    else:
        clear()
        print(f"{guess} is correct!")

    # Check if guess matches anywhere in word
    for idx in range(len(chosen_word)):

        letter = chosen_word[idx].lower()

        if letter == guess:

            display[idx] = letter

    # Calculate if game is over - Lose
    if "_" in display and lives_left <= 0:
        game_over = True
        print(f"\nYou Lose 😭. The answer was: {chosen_word}")

    # Calculate if game is over - Win
    if "_" not in display:
        clear()
        print(f"\nYou Win! 🎉. The answer is:\n {chosen_word}")
        game_over = True
