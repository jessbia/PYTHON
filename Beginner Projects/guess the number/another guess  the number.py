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


