'''Hesed Guwn
02/08/22
CS 152 A
Lab 01'''

from re import X

def ballistic1(t):
    '''This function calculates the position of an object (pf) given 
       the variables of initial position (pi) velocity (pi) accleration (a)
       and parameter time duration (t)
    '''
    pi = 1
    vi = 11
    a = -10
    pf = pi + (vi*t) + (0.5*a*(t**2))
    return pf

#Task 3e
# y = ballistic1(.5)
# print("f(0.5) is", y)
# y = ballistic1(1)
# print("f(1) is", y)

def ballistic2(pi, vi, a, t):
    #This function serves the same purpose as ballistic1 but has all variables of the equations be set as parameters
    pf = pi + (vi*t) + (0.5*a*(t**2))
    return pf

#Task 4
# y = ballistic2(2, 11, -10, .5)
# print(y)

def computeAndOutput(pi, vi, a, t):
    #This function uses ballistic2(pi,vi,a,t) to compute position while also directing the output into another file (data.csv)
    x = ballistic2(pi,vi, a, t)
    fp = open( 'data.csv', 'a' )
    fp.write( str(t) + ", " + str(x) + "\n" )
    fp.close()
    print(t, " , ", x)

def trajectory10(pi,v,a,ti):
    '''This function computes 10 positions by calling computeAndOutput ten times while adding 0.1 to ti with each call'''
    computeAndOutput(pi,v,a,ti)
    computeAndOutput(pi,v,a,ti+0.1)
    computeAndOutput(pi,v,a,ti+0.2)
    computeAndOutput(pi,v,a,ti+0.3)
    computeAndOutput(pi,v,a,ti+0.4)
    computeAndOutput(pi,v,a,ti+0.5)
    computeAndOutput(pi,v,a,ti+0.6)
    computeAndOutput(pi,v,a,ti+0.7)
    computeAndOutput(pi,v,a,ti+0.8)
    computeAndOutput(pi,v,a,ti+0.9)

#Task 6 trajectory10 check
#trajectory10(1, 11, -10, 0)
#trajectory10(1, 11, -10, 1)
#Matches with what the paper says

def trajectory100(pi,v,a,ti):
    '''This function computes 100 positions by calling trajectory10 ten times while adding 1 to ti with each call'''
    trajectory10(pi,v,a,ti)
    trajectory10(pi,v,a,ti+1)
    trajectory10(pi,v,a,ti+2)
    trajectory10(pi,v,a,ti+3)
    trajectory10(pi,v,a,ti+4)
    trajectory10(pi,v,a,ti+5)
    trajectory10(pi,v,a,ti+6)
    trajectory10(pi,v,a,ti+7)
    trajectory10(pi,v,a,ti+8)
    trajectory10(pi,v,a,ti+9)

#Task 7 trajectory100 check
trajectory100(1,50,-10,0)
#Matches with waht the paper produces

#Task 10 Generating and Plotting 2 Additional Trajectories
'''Using the planetary fact sheet I decided to compare Earth's trajectory with Mars's by setting them in the same inital
   position and time. I couldn't find an accleration so I inputted 1 for both functions. The only thing that is different is 
   the velocity where I inputted the orbital velocity.
'''
#Earth
trajectory100(1,1,1,0)
#Mars
trajectory100(1,0.808,1,0)

'''
Extension
I will attempt to do 2 extensions by writing trajectory1000 and creating a different version of trajectory10 and trajectory100 
that uses loops
'''
def trajectory1000(pi,v,a,ti):
    '''This function computes 100 positions by calling trajcetory100 ten times while adding 10 to ti'''
    trajectory100(pi,v,a,ti)
    trajectory100(pi,v,a,ti+10)
    trajectory100(pi,v,a,ti+20)
    trajectory100(pi,v,a,ti+30)
    trajectory100(pi,v,a,ti+40)
    trajectory100(pi,v,a,ti+50)
    trajectory100(pi,v,a,ti+60)
    trajectory100(pi,v,a,ti+70)
    trajectory100(pi,v,a,ti+80)
    trajectory100(pi,v,a,ti+90)
    '''It seems that I only had to write 13 lines of code including this line and line 80'''

def trajectory10looping(pi,v,a,ti):
    '''Achieves the same purpose as trajectory10 but instead of calling computeAndOutput 
       10 times through brute force, it uses a while loop instead
    '''
    i = 0
    # i is what dictates how much the loop repeats
    n = 0
    # n is the variable that gets added to ti
    while i < 10:
        computeAndOutput(pi,v,a,ti+n)
        n = n + 0.1
        i = i + 1

def trajectory100looping(pi,v,a,ti):
    '''Achieves the same purpose as trajectory100 but instead of calling computeAndOutput 
       10 times through brute force, it uses a while loop instead
    '''
    i = 0
    # i is what dictates how much the loop repeats
    n = 0
    # n is the variable that gets added to ti
    while i < 10:
        trajectory10(pi,v,a,ti+n)
        n = n + 1
        i = i + 1

'''Computing both functions to see if they both produce the same results'''
#trajectory10(1,1,1,1)
#trajectory10looping(1,1,1,1)
'''Results are the same'''

'''Computing both functions to see if they also both produce the same results'''
#trajectory100(1,1,1,1)
#trajectory100looping(1,1,1,1)
'''Results are the same'''

'''Computing this function to see if 1000 points are created'''
#trajectory1000(1,1,1,1)
'''1000 lines of code is generated'''
