''' 
Hesed Guwn
Spring 2022
CS 152 Project 8
4/12/22
'''

''' The goal of this program is to give the user a set of word prompts and then record their answer '''

def main():

    print("Hello, type your responses to the following words ")

    words = ["gym ", "poop ", "potato ", "cat ", "dog ", "Egypt ", "jacket ", "emotion ", "robot ", "human "]
    mapping = {}

    #For loop that iterates through all the words in the list of words
    for word in words:
        
        #shows current word
        print(word)

        #User response to word
        response = input("Type your response: ")

        #Dictionary sets response as the key to the words
        mapping[word] = response

    #For loop that iterates through all the keys in the dictionary
    for keys in mapping.keys():

        #Gets the keys
        keys = mapping.get(keys)

        #Prints out keys
        print(keys)


if __name__ == "__main__":
    main()
