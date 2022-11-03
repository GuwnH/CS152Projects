''' 
Hesed Guwn
Spring 2022
CS 152 Project 2
'''

from audioop import avg


def main():
    
    '''This function uses the for loop to repeatedly read the GoldieMRLCJuly.csv data file and go through every date and 
       temperature recorded in the file to constantly extract the air temperature at 3:03 PM each day into another file 
       extractData.csv through the use of an if statement that decides whether or not the specifc time 3:03 PM is inside 
       the recorded date
    '''

    #For an easier way to keep track of corresponding temperature and cleaner columns, I decided to make a day variable
    day = 0

    temp = 0

    fp = open("GoldieMLRCJuly.csv", "r")
    
    #gp is for where the data from this file will be printed into
    gp = open( 'extractData.csv', 'a' )
    line = fp.readline()
    
    #This is for the head of the two columns we want (the day and the temperature of the day at 3:03 PM)
    gp.write("Day, Temp" + "\n")
    
    #loop that will repeat until there are no more unread lines in GoldieMLRCJuly.csv
    for line in fp:
        
        words = line.split(",")
        
        #The specific time that we want to capture for each day
        wantedTime = "3:03:00 PM"
        
        date = words[0]
        
        #This if statement makes sure that we get the temperature at 3:03 PM specifically
        if wantedTime in date:

            #temp is the current temperature at the current read line
            temp = words[5]

            day = day + 1
            
            #Writes our data down in column format
            gp.write( str(day) + ", " + str(temp) + "\n" )
            
            print(line)
            
            print(str(day) + ", " + str(temp) + "\n")
            

    fp.close()
    gp.close()

# only execute main if this file was executed
if __name__ == "__main__":
    main()