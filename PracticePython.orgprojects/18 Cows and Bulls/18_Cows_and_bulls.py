#Cows And Bulls   
#Exercise 18 
#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.



import random
#creates a random number with 4 digits
magic_number = random.randint(1000,9999)
magic_list =[]
cow = 0 
bull = 0
#im splitting the number in a list and turning it into a string, it will be easier to check whether the user picks correctly
for i in str(magic_number):
    magic_list.append(i)
print(magic_list)

gg = True

while gg == True:
    
    
    result = input('Please enter a number')
    coin = 0 
    for j in magic_list:
        if result == j:
            
            coin = 1
            
        else:
            coin = 0
    
    
    if coin == 0:
        
        bull +=1
    else:
        cow +=1

    print('You have',bull, 'Bulls')
    print('You have', cow, 'Cows')
    
    
    if cow == 4:
        print('You win')
        gg = False
    elif bull == 4:
        print('You lose')
        gg = False

