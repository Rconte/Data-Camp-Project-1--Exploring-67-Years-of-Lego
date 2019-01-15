#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that 
#they will turn 100 years old.

#input user name,age
#year has been set to 2019 
tt = True
while tt == True:
    user = input('What is your name?')
    
    age = int(input('What is your age?'))
    if age <= 0 :
        print('Your age is < 0, please try again')
        tt = False
    else:
        pass
    year = 2019
    in_a_hundred = 100 - age + year
    print('Hello',user, 'The year you will turn 100 is',in_a_hundred)
