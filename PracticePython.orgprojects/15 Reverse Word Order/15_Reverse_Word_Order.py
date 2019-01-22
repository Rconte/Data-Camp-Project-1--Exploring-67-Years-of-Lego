#Reverse Word Order
#Exercise 15 
#Write a program (using functions!) 
#that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#  My name is Michele
#Then I would see the string:

#  Michele is name My
#shown back to me.

#normal_word = str(input('Insert a word, I will spell it backwards for you'))

def crazy_reverse(word):

    revers_it = word[::-1]
    print(revers_it)
    
gg = True
while gg == True:

    say_it = input('Input a word, I will spell it backwards for you')
    crazy_reverse(say_it)

    wanna_leave = input('WANT TO EXIT> || PRESS Y OR YES TO EXIT?').upper()
    
    if wanna_leave == 'Y' or wanna_leave == 'YES':
        break
    else:
        print(' Alright, Go Again! ')
