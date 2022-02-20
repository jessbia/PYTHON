import random

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("Please type a number larger than 0 next time:")
        quit()
        
else:
    print("PLease, type a number ")
    quit()
    
randon_number = random.randint(0, top_range)


while True:
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time: ")
        continue
    
    if user_guess == randon_number:
        print("You got it!")
        break
    else:
        print("You got it wrong!")