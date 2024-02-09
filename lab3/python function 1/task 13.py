import random

def game():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    random_num = random.randint(1, 20)
    guesses = 0

    while True:
        num = int(input("Take a guess: "))
        guesses += 1

        if num == random_num:
            print(f"Good job, {name}! You guessed the number in {guesses} guesses.")
            break
        elif num < random_num:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

game()
          
