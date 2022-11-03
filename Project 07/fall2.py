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
from physics_objects import Block

'''The purpose of this program is the same as the original fall.py program but with the blocks changing color upon collision before dissappearing and allowing the user 
to interact with the program by pressing q to put the ball in the middle of the screen with higher velocities'''

def main():
    '''main function for implementing the test code'''
        
    # create a graphics window
    win = gr.GraphWin("Falling", 500, 500, False)
    win.setBackground("black")

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

    #adds blocks to the screen
    block = pho.Block( win, dx = 10, dy = 3 )
    block1 = pho.Block( win, dx = 10, dy = 3 )
    block2 = pho.Block( win, dx = 10, dy = 3 )
    block3 = pho.Block( win, dx = 10, dy = 3 )
    block4 = pho.Block( win, dx = 10, dy = 3 )
    
    #makes blocks the floor
    block.setPosition(0, 1)
    block1.setPosition(10, 1)
    block2.setPosition(20, 1)
    block3.setPosition(30, 1)
    block4.setPosition(40, 1)
    
    #draws the blocks
    block.draw()
    block1.draw()
    block2.draw()
    block3.draw()
    block4.draw()

    #infinite while loop that keeps the program alive until stopped by user via clicking the screen
    while True:
        # call the ball's update method with a dt of 0.033
        ball.update(0.033)
        
        time.sleep( 0.033 ) # have the animation go at the same speed

        if win.checkKey() == 'q': # did the user type a 'q'?
            ball.setPosition(25,25)
            ball.setVelocity(random.randint(-50,50),random.randint(-50,50))
        
        if win.checkMouse(): # did the user click the mouse?
            break

        #Checks if ball hits blocks and changes the blocks color
        if block.collision(ball) == True:
            block.setColor("purple")

        if block.collision(ball) == True:
            block.setColor("purple")
        
        if block1.collision(ball) == True:
            block1.setColor("purple")

        if block2.collision(ball) == True:
            block2.setColor("purple")
            
        if block3.collision(ball) == True:
            block3.setColor("purple")

        if block4.collision(ball) == True:
            block4.setColor("purple")

        # if the ball is outside the window
        if ball.getPosition()[0] >= win.getWidth() or ball.getPosition()[1] <= 0:

            #reposition the ball to the center of the window
            ball.setPosition(25,25)
           
            # give it a random velocity
            ball.setVelocity(random.randint(-10,10),random.randint(-10,10))
 
    win.close()

if __name__ == "__main__":
    main()