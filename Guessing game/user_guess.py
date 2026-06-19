# import, functions, whlie, if
import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"What is your guess betweem 1 and {x}: "))
        
        if guess > random_number:
            print("Too High")
        elif guess < random_number:
            print("Too low")
    
    print("You WON!!!!!") 


guess(10)