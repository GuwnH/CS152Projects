''' 
Hesed Guwn
Spring 2022
CS 152 Project 8
4/12/22
'''
import graphicsPlus as gr
import physics_objects as pho
import random
import time
import collision as coll
from physics_objects import Ball
from physics_objects import Block
from physics_objects import Triangle

'''The purpose of this program is to create an animated scene of a ball colliding with all the created physics objects as obstacles'''

#To run the file on terminal type in python3 task4.py
#Extension at line 104

def buildObstacles(win):
    '''Creates all of the obstacles in the scene'''

    #Creates the borders
    block1 = pho.Block(win,0,6,1,500,(1,0,90))
    block2 = pho.Block( win,49,6,5,500,(1,0,90))
    block3 = pho.Block( win,1,49,490,1,(100,0,100))
    block4 = pho.Block( win,1,0,50,2,(100,0,100))

    #Creates three triangle obstacles
    tri1 = pho.Triangle(win,5,1,1,(0,0,0))
    tri2 = pho.Triangle(win,5,1,1,(0,0,0))
    tri3 = pho.Triangle(win,5,1,1,(0,0,0))

    #Creates bumpy circles at the corners
    ball1 = pho.Ball(win,5,-30,-40,(100,0,0))
    ball2 = pho.Ball(win,5,48,4,(100,0,0))

    #Sets the positions of the objects
    block1.setPosition(0,6)
    block2.setPosition(49,6)
    block3.setPosition(1,49)
    block4.setPosition(1,0)
    
    tri1.setPosition(10,40)
    tri2.setPosition(40,40)
    tri3.setPosition(25,25)

    ball1.setPosition(2,4)
    ball2.setPosition(48,4)

    #Gives elasticity to objects
    block1.setElasticity(1.2)
    block2.setElasticity(1.2)
    block3.setElasticity(1.2)
    block4.setElasticity(0.6)

    tri1.setElasticity(0.8)
    tri2.setElasticity(0.8)
    tri3.setElasticity(0.8)

    ball1.setElasticity(1)
    ball2.setElasticity(1)

    #Creates list of shapes
    listShapes = [block1,block2,block3,block4,tri1,tri2,tri3,ball1,ball2]

    #Return the list of Things
    return listShapes

def main():
    
    # create a GraphWin
    win = gr.GraphWin("PinBall!!!!", 500, 500, False)
    win.setBackground("white")

    # call buildObstacles, storing the return list in a variable (e.g. shapes)
    shapes = buildObstacles(win)
    # loop over the shapes list and have each Thing call its draw method
    for shape in shapes:
        shape.draw()
    
    # assign dt a value 
    dt = 0.003
    # assign to frame the value 0
    frame = 0
    time.sleep(dt)

    #create a ball, give it an initial velocity and acceleration, and draw it
    # projectile = Ball(win,1,1,1,(0,50,0))
    # projectile.setPosition(18,27)
    # projectile.setVelocity(1,1)
    # projectile.setAcceleration(0.05,0.05)
    # projectile.setElasticity(1)
    # projectile.draw()

    # Uncomment below and comment above to run with gord as a projectile
    # projectile = pho.Gourd(win)
    # projectile.setVelocity(1,1)
    # projectile.setPosition(18,27)
    # projectile.setAcceleration(0.05,0.05)
    # projectile.draw()

    #Extension uncomment below and comment above for projectile to be arrow
    projectile = pho.Arrow(win,1,20,20,(0,0,0))
    projectile.setVelocity(1,1)
    projectile.setAcceleration(0.05,0.05)
    projectile.setPosition(18,27)
    projectile.draw()

    # start an infinite loop
    while True:
        
        # if frame modulo 10 is equal to 0
        if frame % 10 == 0:
            
            # call win.update()
            win.update()
        
        if win.checkKey() == 'q':
            projectile.setColor((random.randint(0,100),random.randint(0,100),random.randint(0,100)))

        # using checKey, if the user typed a 'q' then break
        if win.checkMouse(): # did the user click the mouse?
            break

        # if the ball is out of bounds, re-launch it
        if projectile.getPosition()[0] >= win.getWidth() or projectile.getPosition()[1] >= win.getHeight():
            projectile.setPosition(18,27)
            projectile.setVelocity(1,1)
            projectile.setAcceleration(0.05,0.05)

        # assign to collided the value False
        collided = False

        # for each item in the shapes list
        for shape in shapes:
            
            # if the result of calling the collision function with the ball and the item is True
            collision = coll.collision(projectile,shape,dt)
            if collision == True:
                print("colliding" + shape.getType())
                # set collided to True
                collided = True

        # if collided is equal to False
        if collided == False:
            # call the update method of the ball with dt as the time step
            projectile.update(dt)

        # increment frame
        frame = frame + 1

    # close the window
    win.close()

if __name__ == "__main__":
    main()
