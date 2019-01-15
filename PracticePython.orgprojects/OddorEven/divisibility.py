#Exercise 2

#Ask the user for a number. 
#Depending on whether the number is even or odd,
#print out an appropriate message to the user. 
 
#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. 
#If not, print a different appropriate message.
goagain = True
while goagain == True:
    n_input = int(input('Please select a number'))
    x_input = int(input('Please select another number'))
    print('I will check if ', x_input, ' is divisble by', n_input)
    if n_input % x_input == 0:
        print(x_input, ' is divisble by', n_input)
    else:
        print(x_input, ' is NOT divisble by', n_input)
    at_it = input('Would you like to try again? Type y or yes to continue or any other key to exit')
    if at_it == 'y' or at_it == 'Y' or at_it == 'yes' or at_it == 'Yes':
        goagain = True
    else:
        goagain = False
