''' 
Hesed Guwn
Spring 2022
CS 152 Project 3
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

#computes the mean of the list of data.
def mean(data):
    
    calculatedmean = sum(data) / len(data)
    return calculatedmean

#computes the min of the list of data.
def min(data):

    min = 9999999999999999999999999999999.0
    
    #loop that will repeat until there are no more unread lines in blend.csv
    for values in data:
        
        #this if statement decides if the read temperature is the new high temperature and that the date of this occurence is recorded
        if values < min:
            min = values
    
    return min    


#computes the max of the list of data.
def max(data):

    max = -9999999999999999999999999999999.0
    
    #loop that will repeat until there are no more unread lines in blend.csv
    for values in data:
        
        #this if statement decides if the read temperature is the new high temperature and that the date of this occurence is recorded
        if values > max:
            max = values
    
    return max    


#computes the variance of the list of data.
def variance(data):

    #The mean value of all observations
    xm = mean(data)
    
    #Number of observations
    n = len(data)

    #Starting sum
    sum = 0.0

    #The sum of all differences between observed value and mean squared
    i = 0
    for items in data:
        currentDif = (data[i] - xm) * (data[i] - xm)
        sum = sum + currentDif
        i = i + 1

    calculatedVariance = sum / (n - 1)
    
    return calculatedVariance




if __name__ == "__main__":    
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print("The sum is: " + str(sum(list)))
    print("The max is: " + str(max(list)))
    print("The min is: " + str(min(list)))
    print("The mean is: " + str(mean(list)))
    print("The variance is: " + str(variance(list)))