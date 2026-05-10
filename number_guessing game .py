# import random module to generate random numbers
import random
num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 100. Can you guess it?")
# initialize the number of attempts
guess = int(input("Enter your guess: "))
# using statement to check if the guess is correct
if guess == num:
    print("Congratulations! You guessed the number correctly.")
else:
    print("Sorry, that's not the correct number. try again next time!")