import random 

def computer_guess(x):
    
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'r':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} Higher (H), Lower (L) or Right (R)? ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    
    print("I Won You Humans!!!!")


computer_guess(10)



# Try solving the error hapenning when the argument of computer_guess equals the lowest number (1) 


# The Answer 

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low  # could also be high b/c low = high
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f'Yay! The computer guessed your number, {guess}, correctly!')