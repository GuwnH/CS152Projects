''' 
Hesed Guwn
Spring 2022
CS 152 Lab 3
'''

import sys
import stats

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
    
    # close the data file
    fp.close

    # print data
    print(data)
    print(added)

    return

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
 
