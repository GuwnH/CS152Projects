# template written by Bruce A. Maxwell
# updated by Hesed Guwn
# Spring 2022
# CS 152
# Project 7

import graphicsPlus as gr
import physics_objects as pho
import random
import time
from physics_objects import Ball
# from physics_objects import Block

'''The purpose of this program is to run a physics simulation that tests our ball and block class by displaying our ball falling from the center of the screen to the 
bottom and hitting blocks that disappear on collision with the ball returning back to the middle of the screen upon falling'''


def main():
    '''main function for implementing the test code'''

    # create a graphics window
    win = gr.GraphWin("Falling", 500, 500, False)

    # create a ball
    ball = Ball(win)
    # move it to the center of the screen and draw it
    ball.setPosition(25,25)
    # give it a random velocity
    ball.setVelocity(random.randint(-10,10),random.randint(-10,10))
    # set the acceleration to (0, -20)
    ball.setAcceleration(0,-20)
    # draws the ball in the window
    ball.draw()

    #infinite while loop that keeps the program alive until stopped by user via pressing q or clicking the screen
    while True:
        # call the ball's update method with a dt of 0.033
        ball.update(0.033)
        
        time.sleep( 0.033 ) # have the animation go at the same speed

        if win.checkKey() == 'q': # did the user type a 'q'?
            break
        
        if win.checkMouse(): # did the user click the mouse?
            break

        # if the ball is outside the window
        if ball.getPosition()[0] >= win.getWidth() or ball.getPosition()[1] <= 0:

            #reposition the ball to the center of the window
            ball.setPosition(25,25)
           
            # give it a random velocity
            ball.setVelocity(random.randint(-10,10),random.randint(-10,10))
 
    win.close()

if __name__ == "__main__":
    main()