''' 
Hesed Guwn
Spring 2022
CS 152 Project 4
'''

from operator import truediv
import random
import matplotlib.pyplot as plt
import sys

'''This function intializes the population of penguins given the parameters of initSize which decides the size or length 
   of the list of population and probFem which decides the probability of a penguin being female and then returns the created 
   population'''
def initPopulation(initSize,probFem):

    #Starting empty list of penguin population
    population = []
    
    #Loop that creates the population list of initSize penguins
    for i in range(initSize):

        #Random number between 0 and 1 that decides whether or not a penguin added to the list is female or not
        randomNum = random.random()

        #If statement that decides if penguin is female
        if randomNum < probFem:
            
            population.append("F")
        
        #If statement that decides if penguin is male
        else:
            
            population.append("M")
    
    return population

'''This function simulates the change in penguin population under a year given the parameters pop (the initial population), 
    elNinoProb (probability of the year being El-Nino, stdRho (the growth rate of population under a normal year), elNinoRho 
    (growth rate under an El-Nino year), probFemale (probability of a penguin being female), and maxCapacity (the limit on how
    many penguins are allowed to be in the population) and then returns the updated penguin population'''
def simulateYear(pop,elNinoProb,stdRho,elNinoRho,probFemale,maxCapacity):

    #By default a year is not an El Nino year
    elNinoYear = False

    #If statement that decides based on probability whether or not the simulated year is an El-Nino year or not
    if random.random() < elNinoProb:

        elNinoYear = True

    #Inital list of the new population after a year of simulation
    newpop = []

    #For loop that goes through every penguin in the original population
    for penguin in range(len(pop)):
        
        # if statement that checks if max capacity is reached and breaks the loop if so
        if len(newpop) > maxCapacity:
            
            # break, since we don't want to make any more penguins
            break

        #If statement that checks if the current year is an El Nino Year
        if elNinoYear == True:
            
            #If statement that decides based on probability if a penguin will be added to the population under an El Nino year
            if random.random() < elNinoRho:  
                
                # append the penguin to the new population list
                newpop.append(pop[penguin])

        else:
            
            # append the penguin to the new population list
            newpop.append(pop[penguin])
            
            # if random.random() is less than the standard growth factor - 1.0
            if random.random() < (stdRho - 1.0):    
                
                # if random.random() is less than the probability of a female
                if random.random() < probFemale:
                
                    #Adds female penguin to the population
                    newpop.append('F')
              
                # else
                else:
                    #Adds male penguin to the population
                    newpop.append('M')
    
    return newpop

'''This function runs similarly to simulateYear but on a grander scale with new parameters N (the amount of years to run the 
    simulation) and minViable (the lowest amount of penguins allowed in population before being deemed an unviable population)
    and returns the year number when the simulation ended''' 
def runSimulation( N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable):

    #The current population (Starts as the inital population)
    population = initPopulation(initPopSize,probFemale)

    #The year that the simulation ends (when penguins either make it through entirely or go extinct early)
    endDate = N

    #For loop that runs through the amount of given years N
    for i in range(N):

        #The changed population after going through i years
        newPopulation = simulateYear(population, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity)

        #If statement that decides if the population is above the minimum viable amount
        if len(newPopulation) < minViable:

            #The penguins died at i year
            endDate = i
            break

        #If statement that decides if the population has any males left
        if "M" in newPopulation == False:

            #The penguins died at i year
            endDate = i
            break
        
        #If statement that decides if the population has any females left
        if "F" in newPopulation == False:

            #The penguins died at i year
            endDate = i
            break
        
        #The updated current population after i years
        population = newPopulation
        
        #print(len(population))

    return endDate   

'''This function computes the cumunalitive extinction probability distribution curve given the parameters resultsSim 
    (the list of endDates from a simulation) and N (amount of years the simulation ran) and returns a list of CEPD values'''
def computeCEPD(resultsSim,N):

    #Initial list of CEPD
    listCEPD = []
    
    #For loop that creates a list of 0s that have the same length as the amount of years ran (N)
    for i in range(N):
        
        listCEPD.append(0)

    #For loop that goes through the length of the original extinction list
    for j in range(len(resultsSim)):

        #If statement that sees if an entry inside the results of the simulation list had a simulation where penguins died early
        if resultsSim[j] < N:

            #For loop that runs from the early extinct simulation to N
            for k in range(resultsSim[j],N):

                #Adds 1 to the CEPD entry 
                listCEPD[k] = listCEPD[k] + 1.0
    
    #For loop that goes through the unpolished listCEPD and divides each entry by the length of the simulation results list
    for m in range(len(listCEPD)):

        listCEPD[m] = listCEPD[m] / len(resultsSim)

    return listCEPD    

'''The main function that takes 3 arguments, the file name, the number of simulations you want to run, and the amount of years 
    between el nino years'''
#The terminal command line should look similar to this---> python3 penguin.py NUMBER NUMBER
def main(argv):

    #If statement that makes sure that 3 essential arguments are given in the command line
    if len(argv) < 3:

        print("Error: Write 3 Arguments Next Time")
        sys.exit()

    else:

        #Number of times to run simulation
        numSim = int(argv[1])

        #Numbers between El Nino years
        numsBtwnElNino = int(argv[2])

        #Default Simulation Parameter Variables
        n = 201
        initPopSize = 500
        probFem = 0.5
        probElNino = 1.0 / numsBtwnElNino
        stdRho = 1.188
        elNinoRho = 0.41
        maxCapacity = 2000
        minViable = 10

        #List of extinction years
        simResults = []

        #Loop that runs simulations numSim amount of times
        for i in range(numSim):

            #Gets the number of years that the simulation succesfully ran
            extinctionDate = runSimulation(n,initPopSize,probFem,probElNino,stdRho,elNinoRho,maxCapacity,minViable)

            #Adds the result to list of extinction years
            simResults.append(extinctionDate)

        #Initial count of results where penguins died earlier than wanted
        earlyExtinctionCount = 0
    
        #For loop that runs through the length of sim results
        for j in range(len(simResults)):

            #If statement that checks if an entry had a simulation where penguins died early
            if simResults[j] < n:

                #Counts every entry where early extinction among penguins happened
                earlyExtinctionCount = earlyExtinctionCount + 1
        
        #The probability of penguins going extinct earlier than the wanted years N
        probExtinction = earlyExtinctionCount / numSim

    #print(simResults)

    #print(probExtinction)

    #Gets the CEPD of the simulations
    cEPD = computeCEPD(simResults, n)

    #Prints every 10th CEPD entry
    for i in range(len(cEPD)):

        if (i/10) ==  round(i/10):
            
            print(cEPD[i-1])

    numYearList = []
    #Creates a list of years ran (same length as CEPD)
    for i in range(len(cEPD)):

        numYearList.append(i)

    #X axis of graph
    x = numYearList

    #Y axis of graph
    y = cEPD

    #sets plot with what to use as points
    plt.plot(x,y,'o')
    
    #titles the plot
    plt.title("CEPD under 7-year El Nino Cycles in relation to Years")

    #labels x axis
    plt.xlabel("Year Number")

    #labels y axis
    plt.ylabel("CEPD")
    
    #shows graph
    plt.show()
    
#test function that lets us check our other functions
def test():
    #popsize = 10
    #probFemale = 0.5

    #pop = initPopulation(popsize, probFemale)

    #print( pop )

    #newpop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)

    #print( "El Nino year" )
    #print( newpop )

    #newpop = simulateYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)

    #print( "Standard year" )
    #print( newpop )

    #simulation1 = runSimulation(201,500,0.5,1.0/7.0,1.188,0.41,2000,10)
    #print(simulation1)
    
    #simulation2 = runSimulation(10,500,0.5,0.5,1.188,0.41,2000,10)
    #print(simulation2)
    
    #simulation3 = runSimulation(201,500,0.5,1.0/7.0,1.188,0.41,2000,10)
    #print(simulation3)

    return

if __name__ == "__main__":
    main(sys.argv)
    #test()
