import random

easy_words = ["apple", "train", "tiger", "house", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "building"]

print("Welcome to the password guessing game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty: ").lower().strip()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid difficulty level. Defaulting to easy.")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password!")
print(f"Hint: The password has {len(secret)} letters.")

while True:
    guess = input("Enter your guess: ").strip().lower()
    
    if not guess:
        print("Please enter a valid guess.")
        continue
    
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You've guessed the password in {attempts} attempts.")
        break

    # Position hint (exact matches)
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    
    # Count matching letters (anywhere in word)
    matching_letters = set(guess) & set(secret)
    
    print("Hint:", hint)
    if matching_letters:
        print(f"Letters in the word: {', '.join(sorted(matching_letters))}")
    else:
        print("No matching letters. Try a different word!")

print("Thanks for playing the password guessing game, Game Over!")