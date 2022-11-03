''' 
Hesed Guwn
Spring 2022
CS 152 Project 2
'''

from audioop import avg


def main():
    
    '''This function uses the for loop to repeatedly read the GoldieMRLCJuly.csv data file and go through every date and 
       pAR value recorded in the file to constantly extract the daily pAR at 12:03 PM and through an if statement decide whether
       or not the respective day is sunny or cloudy, which is then used to calculate the total number of sunny and cloudy days and
       their average PAR values for the month.
    '''
    #Total number of sunny days in July
    numSunny = 0

    #Total number of cloudy days in July
    numCloudy = 0

    #The sum of PAR when days were sunny
    sumSunnyPAR = 0

    #The sum of PAR when days were cloudy
    sumCloudyPAR = 0

    #Current PAR value
    pAR = 0

    fp = open("GoldieMLRCJuly.csv", "r")
    line = fp.readline()
    
    #loop that will repeat until there are no more unread lines in GoldieMLRCJuly.csv
    for line in fp:
        print(line)
        words = line.split(",")
        
        #The specific time that we want to capture for each day
        wantedTime = "12:03:00 PM"
        
        date = words[0]

        #This if statement makes sure that we get the PAR at 12:03 PM specifically
        if wantedTime in date:
            pAR = float(words[4])
            
            #These if statements decides whether the day is sunny or cloudy based on how high the PAR is 
            if pAR > 800:
                numSunny = numSunny + 1
                sumSunnyPAR = sumSunnyPAR + pAR
            else:
                numCloudy = numCloudy + 1
                sumCloudyPAR = sumCloudyPAR + pAR
    
    #These expressions calculate the average PAR values for when a day is sunny or cloudy
    avgPARCloudy = sumCloudyPAR / numCloudy
    avgPARSunny = sumSunnyPAR / numSunny

    print("There have been: " + str(numSunny) + " sunny days, with an average PAR of: " + str(avgPARSunny) )
    print("There have been: " + str(numCloudy) + " cloudy days, with an average PAR of: " + str(avgPARCloudy) )

    fp.close()



# only execute main if this file was executed
if __name__ == "__main__":
    main()