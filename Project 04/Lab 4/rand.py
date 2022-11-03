''' 
Hesed Guwn
Spring 2022
CS 152 Project 4
'''

import random
import matplotlib.pyplot as plt

#This function generates a list of parameter N random numbers that range from 0 to 1
def genNrandom(N):
    
    #Starting empty list
    numbers = []
    
    #For loop that repeats the given amount of times wanted
    for i in range(N):
        numbers.append(random.random())
    
    #Gives the list of random numbers
    return numbers

#This function generates parameter N random integers between a parameter lower bound and parameter upper bound
def genNintegers(N, lower, upper):

    #Starting empty list
    numbersList = []

    #For loop that repeats the given amount of times wanted (N)
    for i in range(N):
        numbersList.append(random.randint(lower, upper))
    
    #Gives the list of random numbers
    return numbersList

#This function generates N random values drawn from a normal/Gaussian distribution using parameters mean and std (standard deviation)
def genNormal(N,mean,std):

    #Starting empty list
    numbersList = []

    #For loop that repeats the given amount of times wanted (N)
    for i in range(N):
        numbersList.append(random.gauss(mean, std))
    
    #Gives the list of random numbers
    return numbersList


#This function tests the files functions
def test():
    
    #Lab tasks 1-3
    
    # randomNumbers = genNrandom(10)
    # print(randomNumbers)

    #randomIntegers = genNintegers(10,-10,10)
    #print(randomIntegers)

    #randomFloats = genNormal(10,0,0.2)
    #print(randomFloats)

    #Lab task 4 requires me to name the following variables that calls these functions x,y,z

    x = genNrandom(10)
    y = genNintegers(10,-10,10)
    z = genNormal(10,0,0.2)

    #sets plot with what to use as points
    plt.plot(x,z,'o')
    
    #titles the plot
    plt.title("My first plot Lab 4")

    #labels x axis
    plt.xlabel("X")

    #labels y axis
    plt.ylabel("Y")
    
    #shows graph
    plt.show()

    if()
    else(
        for
    )
    string = ""
    string = str(i) + " + " + str(i) + "= " + str(i**2) +=
    print(string)



test()
