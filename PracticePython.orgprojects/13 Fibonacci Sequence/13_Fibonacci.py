#Fibonacci  
#Exercise 13 (and Solution)
#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fibonacci():
    x =int(input('How many iterations of the Fibonacci Sequence?'))
    frontier = []
    i = 1
    if x == 0:
        frontier = []
    elif x == 1:
        frontier = [1]
    elif x == 2:
        frontier = [1,1]
    elif x>2:
        frontier = [1,1]
        while i < (x-1):
           frontier.append(frontier[i] + frontier[i-1])
           i += 1
    print('Sequence = ', frontier)

fibonacci()
