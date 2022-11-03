''' 
Hesed Guwn
Spring 2022
CS 152 Project 3
'''

from cgi import test

#This extension adds more statistic values to the stats.py file (median, range, and standard deviation)
#The new parts start at line 84

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

    #Number of observations
    n = len(data)
    
    #The mean value of all observations
    xm = mean(data)

    #Starting sum
    sum = 0.0

    #The sum of all differences between observed value and mean squared
    i = 0
    for items in range(len(data)):
        currentDif = (data[i] - xm) * (data[i] - xm)
        sum = sum + currentDif
        i = i + 1

    calculatedVariance = float(sum) / (n - 1)
    
    return calculatedVariance

#computes the median of list of data
def median(data):

    #new list that is the same as parameter list so that the original list is not altered for other functions
    medianData = data[:]
    
    #sets list in numerical order 
    medianData.sort()

    #length of list which will be used to determine how to find median
    length = len(medianData)

    #finds median of even numbered length list
    if (length % 2) == 0:
    
        #loop that goes through every value/item in list
        for i in range(len(medianData)):

            #checks if there are more than 2 numbers on the list
            if len(medianData) > 2:
                
                #removes lowest number
                medianData.remove(medianData[0])
                
                #removes highest number
                medianData.remove(medianData[-1])
            
            #checks if there are exactly 2 numbers left on list
            if len(medianData) == 2:

                #extracts the median of an even numbered length list
                median = (medianData[0] + medianData[1])/2
        
                return median
    
    #finds median of odd numbered length list
    if (length % 2)  != 0:
    
        #goes through every value/item in list
        for i in range(len(medianData)):
            
            #checks if length of list is more than one
            if len(medianData) > 1:
                
                #removes lowest number
                medianData.remove(medianData[0])
                
                #removes highest number
                medianData.remove(medianData[-1])
            
            #checks if length of list is exactly one
            if len(medianData) == 1:

                #extracts the median of odd numbered list
                median = medianData[0]
    
                return median


#computes the standard deviation of (of a sample) list of data, which is square root of variance
def standardDeviation(data):
    
    #obtains variance
    variance1 = variance(data)
    
    #roots the variance to get standard deviation
    standardDev = variance1**(1/2)
    
    return standardDev

#computes the range of list of data which is max-min
#changed name to spread so that the range function for indexies is not affected
def spread(data):
    
    #gets the maxiumum
    highest = max(data)
    
    #gets the minimum
    lowest = min(data)
    
    #computes range
    range1 = highest - lowest
    
    return range1

if __name__ == "__main__":    
    list1 = [4,2,1,5,3]
    list2 = [12,74,46,58,91,23]
    print("The median of list 1 is: " + str(median(list1)))
    print("The median of list 2 is: " + str(median(list2)))
    print("The range of list 1 is: " + str(spread(list1)))
    print("The range of list 2 is: " + str(spread(list2)))
    print("The standard deviation of list 1 is: " + str(standardDeviation(list1)))
    print("The standard deviation of list 2 is: " + str(standardDeviation(list2)))    

    #list3 = [3255737, 4192380, 4227603, 4959672, 5006968, 5416210, 6510131, 7470257, 8148571, 9696358, 10943620, 12938381, 12995181, 13977130, 15462786, 16327832, 16952386, 19368878, 21295304, 21414488, 25994320, 26128913, 27004673, 29349681, 30144911, 30457003, 31729219, 32241593, 32734228, 32840960, 32932239, 33063161, 34050444, 34341585, 34930700, 35282292, 35331028, 35451426, 37587951, 38922141, 39434289, 39864244, 40515350, 40710146, 41312636, 41620423, 41702554, 42040932, 44219356, 45133371, 46969338, 47758752, 50428830, 50868352, 52315456, 54125380, 54326922, 55068034, 55998232, 56488085, 57456709, 57856055, 58511689, 58967197, 60258551, 62613145, 63374133, 64070314, 64378248, 64993916, 65358858, 65775113, 67895726, 69595246, 70457426, 70828713, 72236832, 73105872, 73838707, 74473290, 75879012, 76105175, 76236523, 76951935, 79551562, 82542812, 85832500, 86078975, 87016608, 87847890, 88335885, 89421754, 91936114, 92684604, 93920358, 94136324, 96824684, 98325202, 98775028, 99417590]
    #list4 = [12,74,46,58,91,23]
    #print("The median of list 3 is: " + str(median(list3)))
    #print("The median of list 4 is: " + str(median(list4)))
    #print("The range of list 3 is: " + str(spread(list3)))
    #print("The range of list 4 is: " + str(spread(list4)))
    #print("The standard deviation of list 3 is: " + str(standardDeviation(list3)))
    #print("The standard deviation of list 4 is: " + str(standardDeviation(list4)))
