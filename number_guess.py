#Number guessing game

import random
from replit import clear
import art

def answer():
    answer = random.choice(range(1, 101))
    return answer
print(answer)

def difficulty(choice):
    if choose == 'easy':
        return easy_guess
    else:
        return hard_guess

player_guess = 0
game_answer = 0
game_over = False


while not game_over:
    play_game = input("Type 'y' to play a game or 'n' to exit: ")
    clear()
    easy_guess = 9
    hard_guess = 4
    if play_game == 'n':
        game_over = True
    elif play_game == 'y':
        print(art.logo)
        choose = input("Choose 'easy' for 10 attempts or 'hard' for 5 attempts: ")
        game_answer = answer()
        difficulty(choose)
        
        choice = True
        while choice:
            if choose == 'easy':
                guess = input("Guess a number between 1 and 100: ")
                player_guess = int(guess)
                if player_guess == game_answer:
                    print("Correct, player wins.")
                    choice = False
                elif player_guess > game_answer and easy_guess > 1:
                    print(f"Too high, guess again. # left to guess: {easy_guess}")
                    easy_guess -= 1
                elif player_guess < game_answer and easy_guess > 1:
                    print(f"Too low, guess again. # left to guess: {easy_guess}")
                    easy_guess -= 1
                elif player_guess > game_answer and easy_guess == 1:
                    print("Too high.  Last guess.")
                    easy_guess -= 1
                elif player_guess < game_answer and easy_guess == 1:
                    print("Too low.  Last guess.")
                    easy_guess -= 1
                elif easy_guess == 0:    
                    print(f"You're out of guesses.  The answer was {game_answer}. You lose.")
                    choice = False
        
            elif choose == 'hard':
                guess = input("Guess a number between 1 and 100: ")
                player_guess = int(guess)
                if player_guess == game_answer:
                    print("Correct, player wins.")
                    choice = False
                elif player_guess > game_answer and hard_guess > 1:
                    print(f"Too high, guess again. # left to guess: {hard_guess}")
                    hard_guess -= 1
                elif player_guess < game_answer and hard_guess > 1:
                    print(f"Too low, guess again. # left to guess: {hard_guess}")
                    hard_guess -= 1
                elif player_guess > game_answer and hard_guess == 1:
                    print("Too high.  Last guess.")
                    hard_guess -= 1
                elif player_guess < game_answer and hard_guess == 1:
                    print("Too low.  Last guess.")
                    hard_guess -= 1
                elif hard_guess == 0:    
                    print(f"You're out of guesses.  The answer was {game_answer}. You lose.")
                    choice = False 