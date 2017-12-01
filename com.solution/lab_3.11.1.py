# Painting the wall
import math

# Dictionary of paint colors and cost per gallon
paintColors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wallHeight = float(input('Enter wall height (feet): \n'))
wallWidth = float(input('Enter wall width (feet): \n'))
wallArea = wallHeight * wallWidth
print('Wall area:', wallArea, 'square feet')

# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
print('Paint needed:', wallArea / 350, 'gallons')

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
print('Cans needed:', math.ceil(wallArea/350), 'can(s)\n')

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
paintColor = input('Choose a color to paint the wall: \n')
paintCost = {'red' : '35', 'blue' : '25', 'green' : '23'}
paintFinalCost =  int(paintCost[paintColor]) *  math.ceil(wallArea/350)
print('Cost of purchasing', str(paintColor),  'paint:', '$' + str(paintFinalCost))
