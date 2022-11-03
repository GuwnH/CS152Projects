''' 
Hesed Guwn
Spring 2022
CS 152 Project 3
'''

def density(temps):
    
    #This function takes a list of temperatures, computes density from the list, and creates a list of densities.

    densityList = []
    #i is a looping variable that extracts the index of each value in the list
    i = 0
    for items in temps:
        
        #the value of the current index of temperature list
        t = temps[i]
        
        #expression that calculates the density 
        rho = 1000 * (1 - (t + 288.9414) * (t - 3.9863)**2 / (508929.2*(t + 68.12963)))
        
        #adds to the list of density
        densityList.append(rho)

        #lets i move on to the next index
        i = i + 1
    
    return densityList

def thermocline_depth( temps, depths ):
    
    #this function computes the derivative of density with respect to depth

    # assign to rhos the result of calling the density function with temps as the argument
    rhos = density(temps)
    
    # assign to drho_dz the empty list
    drho_dz = []
    
    # loop for one less than the length of rhos
    for i in range(len(rhos)-1):

        # append to drho_dz the quantity rhos[i+1] minus rhos[i] divided by the quantity depths[i+1] minus depths[i]
        drho_dz.append((rhos[i+1] - rhos[i]) / (depths[i+1] - depths[i]))
        # optional step: print out temps[i], rhos[i], and drho_dz[i]
        #print(temps[i])
        #print(rhos[i])
        #print(drho_dz[i])
            
        # assign to max_drho_dz the value -1.0
        max_drho_dz = -1.0
        # assign the maxindex the value -1
        maxindex = -1
        # loop for the length of drho_dz (loop variable i)
        for i in range(len(drho_dz)):
            # if drho_dz[i] is greater than max_drho_dz
            if drho_dz[i] > max_drho_dz:
            
                # assign to max_drho_dz the value drho_dz[i]
                max_drho_dz = drho_dz[i]
            
                # assign to maxindex the value i
                maxindex = i
            
    #assign to thermoDepth the average of depths[maxindex] and depths[maxindex+1]
    thermoDepth = (depths[maxindex] + depths[maxindex+1]) / 2

    return thermoDepth

def main():
    '''This function reads data from GoldieJuly2019, extracts all temperature fields in order, and computes 
    the thermolcine_depth and prints the thermocline_depth value'''
    
    # these are the fields corresponding to the temperatures in order by depth
    # note they use 0-indexing
    fields = [10, 11, 16, 17, 15, 14, 13, 12]

    # these are the depth values for each temperature measurement
    depths = [ 1, 3, 5, 7, 9, 11, 13, 15 ]

    # open the data file and read past the header line
    fp = open("GoldieJuly2019.csv", "r")

    #creates a data file to write into
    gp = open( 'thermoclineData.csv', 'a' )

    #This is for the header of the two columns we want (the day and the thermocline depth of the day at 12:03 PM)
    gp.write("Day, Thermo Depth" + "\n")

    # assign to day the value 0
    day = 0
    
    line = fp.readline()
    # for each line in the file
    for line in fp:
    
        # split the line on commas and assign it to words
        words = line.split(",")
        date = words[0]
        # if the time is about noon (12:03:00 PM)
        if "12:03:00 PM" in date:
            
            # add one to the day variable
            day = day + 1
        
        # assign to temps the empty list
            temps = []

        # loop over the number of items in depths (loop variable i)
            for i in range(len(depths)):
    
            # append to temps the result of casting words[ fields[i] ] to a float
                temps.append(float(words[fields[i]]))
            
            # assign to thermo_depth the result of calling thermocline_depth with temps and depths as arguments
            thermo_depth = thermocline_depth(temps, depths)

            # prints/save to a file the day of the month and thermo_depth separated by a comma
            print(str(day) + ", " + str(thermo_depth))
            gp.write( str(day) + ", " + str(thermo_depth) + "\n" )

    return

if __name__ == "__main__":
    main()