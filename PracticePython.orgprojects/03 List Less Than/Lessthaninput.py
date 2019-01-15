#Exercise 3 
#Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list
#that are less than 5.

#Extras:

#Instead of printing the elements one by one, 
#make a new list that has all the elements less than 5 
#from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only 
#elements from the original list a that are smaller than that 
#number given by the user.

gg = True
while gg == True:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    print('List stored in memory is ', a)

    user_inpt = int(input('Please insert a number, and I will return a list with elements less than that number'))
    if user_inpt is not int:
        print('You have not inserted an integer')
        gg = False
    else:
        pass
    for index in a:
        if index < user_inpt:
            b.append(index)
    else:
        pass
    print('These elements are less than', user_inpt,':',b)
    gg = False
