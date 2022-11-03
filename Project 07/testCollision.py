# Test function written by Bruce A. Maxwell
# Fall 2019
# CS 152
# Project 7

import graphicsPlus as gr
import physics_objects as pho
import random
import time

'''The purpose of this program is to test the collision method for blocks from the physics_objects.py file'''

def main():
    '''This function creates a window that shows text that tells the user if the ball and block are touching/colliding'''

    #Creates window
    win = gr.GraphWin("Intersections", 500, 500, False)
    win.setBackground("white")

    # make a ball
    ball = pho.Ball( win )

    # make a block
    block = pho.Block( win, dx = 6, dy = 3 )
    block.setPosition(25, 25)
    block.draw()

    # move it to the center of the screen
    ball.setPosition( 25, 25 )
    ball.draw()

    #Creates text
    textbox = gr.Text( gr.Point( 250, 50 ), "Clear" )
    textbox.draw(win)

    # is it colliding?
    if block.collision( ball ):
        textbox.setText( 'Collision' )

    while True:
        time.sleep( 0.033 )

        key = win.checkKey()
        if key == 'q':
            break
        elif key == 'space':
            ball.setPosition( random.randint( 15, 35), random.randint(15, 35) )
            if block.collision( ball):
                textbox.setText( 'Collision' )
            else:
                textbox.setText( 'Clear' )
            
        if win.checkMouse():
            break

    win.close()

if __name__ == "__main__":
    main()