#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, 
#or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

gg = True
guesses = 0
gen_rando = random.randint(0,9)

while gg == True:
    #generates a random number between 1 and 9
    
    player_num = int(input('Rules are simple, find the magic number! Please enter a number between 0 and 9'))
    print('\t')
    # Start by excluding incorrect inputs, program will shut down if number is negative or larger than 10 (excercise specifies we want a number between 1 and 9)
    if player_num < 0 or player_num >10:
        print('Number too high or too low, please start the program again')
        print('\t')
        gg = False
    if player_num > gen_rando:
        print('Your number is too high, try again')
        print('\t')
        guesses += 1
    elif player_num< gen_rando:
        print('Your number is too low, try again')
        print('\t')
        guesses += 1
    else:
        print('You got the number correct, Congratulations! You had', guesses, 'guesses before finding the magic number, the magic number was', gen_rando)
        print('\t')
        gg = False

    #if user presses exit, program closes.
    print('\t')
    play_again = input('Do you want to continue/ (PRESS EXIT TO CLOSE THE PROGRAM)').lower()
    if play_again == 'exit':
        gg = False
    else:
        pass
