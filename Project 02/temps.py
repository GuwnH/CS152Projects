''' 
Hesed Guwn
Spring 2022
CS 152 Project 2
'''

def main():
    
    hiAirTemp = -200
    hidate = ""
    lowAirTemp = 200
    hiWaterTemp = -200
    lowWaterTemp = 200

    fp = open("GoldieMLRCJuly.csv", "r")
    line = fp.readline()
    for line in fp:
        print(line)
        words = line.split(",")
        airTemp = float(words[5])
        date = words[0]
        waterTemp = float(words[1])
        if airTemp > hiAirTemp:
            hiAirTemp = airTemp
            hidate = date
        if airTemp < lowAirTemp:
            lowAirTemp = airTemp
            lowdate = date
        if waterTemp > hiWaterTemp:
            hiWaterTemp = waterTemp
            hidate = date
        if waterTemp < lowWaterTemp:
            lowWaterTemp = waterTemp
            lowdate = date
        print("The Highest Air Temperature of %.3f degrees Celcius ocurred on %s ." % (hiAirTemp,hidate))
        print("The Lowest Air Temperature of %.3f degrees Celcius ocurred on %s." % (lowAirTemp,lowdate))
        print("The Highest Water Temperature of %.3f degrees Celcius ocurred on %s ." % (hiWaterTemp,hidate))
        print("The Lowest Water Temperature of %.3f degrees Celcius ocurred on %s." % (lowWaterTemp,lowdate))
    fp.close()



# only execute main if this file was executed
if __name__ == "__main__":
    main()