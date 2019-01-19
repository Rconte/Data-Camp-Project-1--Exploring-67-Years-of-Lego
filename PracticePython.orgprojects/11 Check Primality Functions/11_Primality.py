

#Check Primality Functions   
#Exercise 11 (and Solution)
#Ask the user for a number and determine whether the number is prime or not. 
#(For those who have forgotten, a prime number is a number that has no divisors.). 
#You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


#def is_it_prime():
def prime_or_not():
    if number ==2 or number == 3 or number == 5 or number==7 or number==11 :
        print(number, 'Number is PRIME')
        
    elif number %2 == 0 or number %3 == 0 or number %5 == 0 or number%7 == 0 or number%11 == 0:
        print('Number is NOT PRIME')
        
    else:
        print('Number is PRIME')
        

gg = True

while gg == True:

    number = int(input("Please enter a number, i will tell you if it is PRIME"))
    if number < 0:
        print('Please enter a positive integer.\n PROGRAM WILL EXIT')
        gg = False
    else:
        pass

    prime_or_not()
    gg = False


