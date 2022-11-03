''' 
Hesed Guwn
Spring 2022
CS 152 Lab 3
'''

from cgi import test

#this function adds up all the values in the list into one sum
def sum(numbers):

    #variable that holds the sum
    calculatedsum = 0.0

    #loop that calculates and updates the sum
    for values in numbers:

        calculatedsum = calculatedsum + values

    return calculatedsum

#this function is for me to test sum(numbers)
def test():

    numList = [1,2,3,4]
        
    sumNumList = sum(numList)

    print(sumNumList)


if __name__ == "__main__":    
    test()
