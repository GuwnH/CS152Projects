''' 
Hesed Guwn
Spring 2022
CS 152 Project 7
4/5/22
'''

from numpy import block
import graphicsPlus as gr
import time
import random

'''The purpose of this program is to create class ball and blocks which will implement physics properties and will be used to create ball and block objects in other 
files'''

class Ball:
    '''Class that creates a ball'''

    def __init__(self,win):
        '''Sets up the initial properties of the ball object'''

        self.mass = 1
        self.radius = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win
        self.scale = 10
        self.vis = [ gr.Circle( gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]*self.scale)),self.radius * self.scale ) ]

    def draw(self):
        '''Draws the ball into the screen'''

        for item in self.vis:
            item.setFill("blue")
            item.draw(self.win)

    def getPosition(self): 
        ''' returns a 2-element tuple with the x, y position.'''
        return (self.position[0],self.position[1])

    def setPosition(self, px, py):
        '''Chnages the position of the ball and moves it accordingly'''

        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]

        # assign to the x coordinate in self.pos the new x coordinate
        self.position[0] = px
        # assign to the y coordinate in self.pos the new y coordinate
        self.position[1] = py

        newX = self.position[0]
        newY = self.position[1]

        # assign to dx the change in the x position times self.scale
        dx = (newX - x_old ) * self.scale
        # assign to dy the change in the y position times -self.scale
        dy = (newY - y_old) * (self.scale * -1)
        # for each item in the vis field of self
        for item in self.vis:
            # call the move method of the item, passing in dx and dy
            item.move(dx,dy)
            
        return self.position[:]

    def getVelocity(self): 
        '''returns a 2-element tuple with the x and y velocities. '''
        velocity = self.velocity[:]
        return (velocity[0],velocity[1])

    def setVelocity(self, vx, vy): 
        '''vx and vy are the new x and y velocities'''
        self.velocity = [vx,vy]
        return self.velocity[:]

    def getAcceleration(self): 
        '''returns a 2-element tuple with the x and y acceleration values.'''
        acceleration = self.acceleration[:]
        return acceleration

    def setAcceleration(self, ax, ay): 
        '''ax and ay are new x and y accelerations.'''
        self.acceleration = [ax,ay]
        return self.acceleration[:]

    def getMass(self): 
        '''Returns the mass of the object as a scalar value'''
        mass = self.mass
        return mass

    def setMass(self, m): 
        '''m is the new mass of the object'''
        self.mass = m
        return self.mass

    def getRadius(self): 
        '''Returns the radius of the Ball as a scalar value'''
        radius = self.radius
        return radius

    def update(self, dt):
        '''This function implements newtonian physics to the object'''
        # assign to x_old the current x position
        x_old = self.position[0]
        # assign to y_old the current y position
        y_old = self.position[1]

        # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = x_old + self.velocity[0]*dt + 0.5*self.acceleration[0] * dt*dt
        # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[1] = y_old + self.velocity[1]*dt + 0.5*self.acceleration[1] * dt*dt
        # assign to dx the change in the x position times self.scale
        dx = (self.position[0] - x_old) * self.scale
        # assign to dy the change in the y position times -self.scale
        dy = (self.position[1] - y_old) * -self.scale
        # for each item in self.vis
        for item in self.vis:
            # call the move method of the graphics object with dx and dy as arguments..
            item.move(dx,dy)

        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = self.velocity[0] + (self.acceleration[0] * dt)
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] = self.velocity[1] + (self.acceleration[1] * dt)

        return self.velocity[:]