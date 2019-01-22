
#List Remove Duplicates  
#Exercise 14 
#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.
import random


def duplicate_remove(list_rando):
    new_list = []
    for i in list_rando:
    
        if i not in new_list:
            new_list.append(i)
    return new_list
    
#Creates a random list, with random integers
list_rando = []
for i in range(random.randint(5,30)):
    list_rando.append(random.randint(1,100))
list_rando.sort()

x = list_rando
print(x)
duplicate_remove(x)
print(duplicate_remove(x))


