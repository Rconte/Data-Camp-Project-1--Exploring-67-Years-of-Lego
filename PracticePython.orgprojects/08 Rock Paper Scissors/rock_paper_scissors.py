#Exercise 8 
#Make a two-player Rock-Paper-Scissors game. 
#(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
#and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock


#Because I really don't want to input the second player's choice (I want that PVE feel for the rock paper scisssors game), I'm going to randomize player 2's choice, this can be easily changed to a player input.
import random


gg = True
while gg == True:

    #player 2 (the computer) chooses his move from the pool (list) of moves we have for the game
    moves = ['Rock', 'Paper','Scissors']
    player2_move = random.choice(moves)
    
    player_move = input('Choose Rock, Paper or Scissors').lower()
    print('You chose ',  player_move)
    

    #both players have chosen their move, let's check for different scenarios, who wins and who loses?
    if player2_move == 'Rock' and player_move == 'paper':
        print('Player 2 chose', player2_move)
        print('You Win')

    elif player2_move == 'Paper' and player_move == 'scissors':
        print('Player 2 chose', player2_move)
        print('You Win')

    elif player2_move == 'Scissors' and player_move == 'rock':
        print('Player 2 chose', player2_move)
        print('You Win')
    elif player2_move == player_move:
        print('Player 2 chose', player2_move)
        print('Tie')
    else:
        print('Player 2 chose', player2_move)
        print('You loose')
    
    
    #Gives the player the choice to play again and stay in the while loop
    play_again = input('Do you want to play again?').lower()
    if play_again == 'y' or play_again== 'yes':
        print('Again and again..')
        pass
    else:
        print('Thanx for playing, gg')
        gg = False
    
   
