''' 
Hesed Guwn
Spring 2022
CS 152 Project 7
4/5/22
'''

import graphicsPlus as gr
import time
import random

'''The purpose of this program is to run very basic zelle graphics windows with very basic functions'''

def test1():
    '''This function creates a window with a circle in the middle'''

    #Creates window
    win = gr.GraphWin( 'My First Window WhooHoo', 500, 500, False )
    win.setBackground("Black")
    
    #Creates point for circle to go to
    point = gr.Point(250,250)
    
    #Creates circle
    circle = gr.Circle(point,10)
    circle.setFill("Red")
    circle.draw(win)

    #Updates window
    win.update()
    point2 = win.getMouse()

    #Gives the value of where the mouse was when clicked
    xValue = point2.getX()
    yValue = point2.getY()
    print(str(xValue) + ", " + str(yValue))

    #Closes window
    win.close()

def test2():
    '''This function creates a window that generates a random moving circle upon clicking the screen'''

    #Makes the windows
    win = gr.GraphWin( 'My Second Window WhooHoo', 500, 500, False )
    win.setBackground("black")

    #Creates list of shapes
    shapes = []

    #Infinite loop that keeps the window open until user presses q
    while True:

        #Checks position of the mouse
        pos = win.checkMouse()

        #If user clicks then random moving blue circle appears
        if pos != None:
            
            circle = gr.Circle(pos,10)
            circle.setFill("blue")
            shapes.append(circle)
            circle.draw(win)

        #Checks for which keyboard key is pressed
        key = win.checkKey()

        #Breaks the loop if user presses q
        if key == 'q':

            break

        #Updates the window screen
        win.update()
        #Gives slight delay at 0.033 seconds
        time.sleep(0.033)
        
        #Moves the circles that exist
        for shape in shapes:

            shape.move(random.randint(-50,50), random.randint(-50,50))
    
    #Closes window
    win.close()

if __name__ == "__main__":
    #test1()
    test2()
