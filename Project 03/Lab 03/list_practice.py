''' 
Hesed Guwn
Spring 2022
CS 152 Lab 3
'''

from asyncio import format_helpers


def main():
    
    #L2 Working with lists
    numbers = [5, 3, 6, 1, 2]
    my_empty_list = []

    numbers.append(7)
    print(numbers)

    first_number = numbers[0]
    fourth_number = numbers[3]
    
    print(first_number)
    print(fourth_number)

    numbers[0] = 4
    print(numbers)

    #L2 Modify the value of two other locations in the list in your Python file
    numbers[2] = 200
    numbers[1] = 300
    
    print(numbers)

# only execute main if this file was executed
if __name__ == "__main__":
    main()