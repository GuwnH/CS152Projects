''' 
Hesed Guwn
Spring 2022
CS 152 Project 2
'''

def main():
    '''This function uses the for loop to repeatedly read the blended data file and go through every date and temperature recorded
       in the file to constantly decide through the use of an if statement whether the temperature corresponding to the date is
       the highest temperature while also keeping in mind the date when the highest temperature was recorded.
    '''

    '''hitemp needs to start somewhere so a large negative number is an easy way to get an initial high temperature that can be 
       compared to other temperatures that are actually high
    '''
    hitemp = -200
    #same logic with hidate but nothing needs to be compared to, just need an empty string
    hidate = ""

    #opens blend data
    fp = open("blend.csv", "r")
    line = fp.readline()
    
    #loop that will repeat until there are no more unread lines in blend.csv
    for line in fp:
        print(line)
        words = line.split(",")

        #temp is the current temperature at the current read line
        temp = float(words[3])
        
        #date is the current date at the current read line
        date = words[0]
        
        #this if statement decides if the read temperature is the new high temperature and that the date of this occurence is recorded
        if temp > hitemp:
            hitemp = temp
            hidate = date
        print("The Highest Temperature of %.3f ocurred on %s." % (hitemp,hidate))
    fp.close()



# only execute main if this file was executed
if __name__ == "__main__":
    main()

