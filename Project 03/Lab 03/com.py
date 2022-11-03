''' 
Hesed Guwn
Spring 2022
CS 152 Lab 3
'''

import sys

#L4 Discover Command Lines Arguments

def main():

    print(sys.argv)
    
    print("Running program", sys.argv[0])
    
    print("I'm going to open the file" , sys.argv[1])
    
    print("I'm going to extract column", int(sys.argv[2]))



if __name__ == "__main__":
    main()
