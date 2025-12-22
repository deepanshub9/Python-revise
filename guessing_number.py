import random

secret_number = random.randint(1, 10)
guesses_left = 3

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10")

while guesses_left > 0:
    print(f"You have {guesses_left} guesses left")
    guess = int(input("What's your guess? "))
    
    if guess == secret_number:
        print("🎉 You won! You found my secret number!")
        break
    elif guess < secret_number:
        print("Too low! Try a bigger number")
    else:
        print("Too high! Try a smaller number")
    
    guesses_left = guesses_left - 1

if guesses_left == 0:
    print(f"Game Over! The secret number was {secret_number}")