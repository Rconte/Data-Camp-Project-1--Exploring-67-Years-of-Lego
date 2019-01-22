#Password Generator

#Exercise 16 
#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

#Extra:

#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import string
import random


def normalChoice():
    wording = []
    
    for i in range(random.randint(10,30)):
        randoletter = random.choice(string.ascii_letters)
        wording.append(randoletter)
        
    k = list(wording)
    print('Your Password is : '.upper(),''.join(k))
   
def strongChoice():
    wording = []
    
    for i in range(random.randint(10,30)):
        let_it_spin = random.randint(0,2)
        if let_it_spin == 1:
            randoletter = random.choice(string.ascii_letters)
            wording.append(randoletter)
        else:
            randonumber = random.randint(0,10)
            wording.append(str(randonumber))
  
    k = list(wording)
    
    print('Your password is : '.upper() ,''.join(k))
    


print('PLEASE SELECT N OR NORMAL FOR A NORMAL PASSWORD (ALPHA ONLY) \n \n OR \n \n S OR STRONG FOR A STRONG SECURITY PASSWORD (ALPHANUMERICAL)')
print('\n')
what_king = input('What kind of password would you like || Normal or Strong?').lower()
print('\n')

gg = True
while gg == True:

    if what_king == 'n' or what_king == 'normal':
        print('You selected normal')
        normalChoice()
        
        break
    elif what_king == 's' or what_king == 'strong':
        print('You selected a strong password')
        strongChoice()

        break
    else:
        print('WRONG INPUT, TRY AGAIN')
        break



