'''Hesed Guwn
02/08/22
CS 152 A
Lab 01'''

print( 'version 1' )
print( 'sum', 42 + 21 + 5 )
print( 'avg', (42 + 21 + 5) / 3 ) 	

def myfunction(a, b, c):
    # Adds the sum of the three parameters
    print('sum', + a + b + c)

myfunction(4,5,6)
# Was told to use the function again with different arguments
myfunction(2,2,10)

print( 'version 2' )
print( 'sum', 42 + 21 + 5 )
print( 'avg', (42 + 21 + 5) // 3 ) 	

print( 'version 3' )
print( 'sum', 42 + 21 + 5.0 )
print( 'avg', (42 + 21 + 5) // 3.0 ) 	

print( 'version 4' )
a = 42
b = 21
c = 5
print( 'sum', a + b + c )
print( 'avg', (a + b + c) // 3.0 )

print('version 5')
a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")

a = int(a)
b = int(b)
c = int(c)
print( 'sum', a + b + c )
print( 'avg', (a + b + c) // 3.0 )

print('version 6')
def stats( a, b, c ):
    print( 'sum', a + b + c )
    print( 'avg', (a + b + c) // 3.0 )

stats( 42, 21, 5 )
stats( 52, 91, 12 )

