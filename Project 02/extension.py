''' 
Hesed Guwn
Spring 2022
CS 152 Project 2
'''

'''Instead of looking at PAR at just noon, try looking at multiple times of day and using the
average. How different are your counts of sunny/cloudy days using different times or
combinations of times?'''

from audioop import avg


def main():
    
    '''This function uses the for loop to repeatedly read the GoldieMRLCJuly.csv data file and go through every date and 
       pAR value recorded in the file to constantly extract the daily pAR at a time range from 10:03 AM to 3:03 PM and 
       through an if statement decide whether or not the respective day is sunny or cloudy, which is then used to calculate 
       the total number of sunny and cloudy days and their average PAR values for the month.
    '''
    

    #Total number of sunny days in July
    numSunny = 0

    #Total number of cloudy days in July
    numCloudy = 0

    #The sum of PAR when days were sunny
    sumSunnyPAR = 0

    #The sum of PAR when days were cloudy
    sumCloudyPAR = 0

    #Current PAR values to their wanted respective times
    pAR1 = 0
    pAR2 = 0
    pAR3 = 0
    pAR4 = 0
    pAR5 = 0
    pAR6 = 0
    
    #The average PAR value for the day
    avgPAR = 0

    #The average PAR values for sunny and cloudy days
    avgPARCloudy = 0
    avgPARSunny = 0

    fp = open("GoldieMLRCJuly.csv", "r")
    line = fp.readline()
    
    #loop that will repeat until there are no more unread lines in GoldieMLRCJuly.csv
    for line in fp:
        print(line)
        words = line.split(",")
        
        #The specific times that we want to capture for each day
        wantedTime1 = "10:03:00 AM"
        wantedTime2 = "11:03:00 AM"
        wantedTime3 = "12:03:00 PM"
        wantedTime4 = "1:03:00 PM"
        wantedTime5 = "2:03:00 PM"
        wantedTime6 = "3:03:00 PM"

        #This specific time is used to make sure that we are calculating the end of the day before PARs gets recalculated and changed
        wantedTime7 = "12:03:00 AM" 
        
        date = words[0]

        #These if statements makes sure that we get the PAR at our wanted times specifically
        if wantedTime1 in date:
            pAR1 = float(words[4])
        if wantedTime2 in date:
            pAR2 = float(words[4])
        if wantedTime3 in date:
            pAR3 = float(words[4])
        if wantedTime4 in date:
            pAR4 = float(words[4])
        if wantedTime5 in date:
            pAR5 = float(words[4])
        if wantedTime6 in date:
            pAR6 = float(words[4])
        
        #This expression calculates the average PAR for the day
        avgPAR = ( pAR1 + pAR2 + pAR3 + pAR4 + pAR5 + pAR6 ) / 6
        
        #This is for me to keep track to see if calcuations and code are looking correct
        #print(avgPAR)

        #This if statement makes sure that we get to decide if the day is sunny or cloudy before the PAR gets changed to a different day
        if wantedTime7 in date:
            
            #These if statements decides whether the day is sunny or cloudy based on how high the PAR is 
            if avgPAR > 800:
                numSunny = numSunny + 1
                sumSunnyPAR = sumSunnyPAR + avgPAR
            if avgPAR <= 800:
                numCloudy = numCloudy + 1
                sumCloudyPAR = sumCloudyPAR + avgPAR

            '''These if statements calculate the average PAR of sunny and cloudy days while taking into account when there is no
               current sunny or cloudy day
            '''
            if numCloudy == 0:
                avgPARCloudy = sumCloudyPAR / 1
            if numSunny == 0:
                avgPARSunny = sumSunnyPAR / 1
            else:
                avgPARCloudy = sumCloudyPAR / numCloudy
                avgPARSunny = sumSunnyPAR / numSunny

    print("There have been: " + str(numSunny) + " sunny days, with an average PAR of: " + str(avgPARSunny) )
    print("There have been: " + str(numCloudy) + " cloudy days, with an average PAR of: " + str(avgPARCloudy) )

    fp.close()

# only execute main if this file was executed
if __name__ == "__main__":
    main()