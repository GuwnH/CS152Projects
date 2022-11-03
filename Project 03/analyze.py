''' 
Hesed Guwn
Spring 2022
CS 152 Project 3
'''

import sys
import stats

#This function computes the mean, median, variance, max, and min of referenced files through the use of command line arguments

def main(filename, column_id):
    
    # assign to fp the result of opening the file hurricanes.csv for reading
    fp = open(filename, "r")
    
    # assign to line the first line of the data file
    line = fp.readline()
    
    # assign to headers the result of splitting the line using commas
    headers = line.split(",")
    
    # print headers
    print(headers)
    
    # assign to data an empty list
    data = []
    
    # for all of the lines in the file
    for line in fp:
        
        # assign to words the result of splitting the line using commas
        words = line.split(",")
        
        # append second item to data (which index?) in words cast as a float
        data.append(float(words[column_id]))

    #find the sum of items inside data
    added = stats.sum(data)

    #finds the mean of items inside data
    average = stats.mean(data)

    #finds the max of items inside data
    max = stats.max(data)

    #finds the min of items inside data
    min = stats.min(data)

    #finds the variance of items inside data
    variance = stats.variance(data)
    
    # close the data file
    fp.close

    # print data
    print(data)
    print("The sum is: " + "%.2f" % added)
    print("The mean is: " + "%.2f" % average)
    print("The variance is: " + "%.2f" % variance)
    print("The minimum is: " + "%.2f" % min)
    print("The maximum is: " + "%.2f" % max)
    
    return

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
 
