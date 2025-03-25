from random import randint
from number_pic import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def difficulty_level( ):
     level = input("Choose a difficulty . Type 'easy' or 'hard': ")
     if level == "easy":
        global turns
        turns = EASY_LEVEL_TURNS
     else:
        turns = HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    answer = randint(1, 100)
    print(f"pssst, the correct answer is {answer}")



    turns = difficulty_level()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Make a guess:"))
        
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You're run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")
game()


