''' 
Hesed Guwn
Spring 2022
CS 152 Project 2
'''

from audioop import avg

"For task 6 I will calculate the % change of daily windspeed from 12:03 AM to 12:03 PM"

def main():
    
    '''This function uses the for loop to repeatedly read the GoldieMRLCJuly.csv data file and go through every date and 
       windspeed recorded in the file to constantly extract the daily windpseed at 12:03 AM and 12:03 PM through an if
       statement that makes sure that our wanted data comes from our wanted times. Once the daily windspeed is found for both
       times, their % change (the relative change between two points of value) is calculated.
    '''

    #Defining needed variables with artifical values to start off with 
    windSpeedAM = 1
    windSpeedPM = 1
    date1 = " "
    date2 = " "

    fp = open("GoldieMLRCJuly.csv", "r")
    line = fp.readline()
    
    #loop that will repeat until there are no more unread lines in GoldieMLRCJuly.csv
    for line in fp:
        
        words = line.split(",")
        
        #The specific times that we want to capture for each day
        wantedTimeAM = "12:03:00 AM"
        wantedTimePM = "12:03:00 PM"

        date = words[0]

        #This if statement makes sure that we get the windspeed at 12:03 AM specifically
        if wantedTimeAM in date:
            
            windspeedAM = float(words[6])
            
            #Holds the date at 12:03 AM speicifically 
            date1 = words[0]
        
        #This if statement makes sure that we get the windspeed at 12:03 PM specifically
        if wantedTimePM in date:
            
            windSpeedPM = float(words[6])

            #Holds the date at 12:03 PM speicifically
            date2 = words[0]
            
            #Calculates the percent change in wind speed between 12:03 AM and 12:03 PM on their specific day
            changeWindSpeed = (( windSpeedPM - windspeedAM ) / (windSpeedAM)) * 100

            #Prints the calculation with the date and time included
            print("Between " + str(date1) + " and " + str(date2) + " % wind speed change is: " + str(changeWindSpeed) + "%")
        
    fp.close()



# only execute main if this file was executed
if __name__ == "__main__":
    main()