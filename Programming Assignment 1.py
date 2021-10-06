# Name: Alexis Faison
# Course: CS151, Prof. Mehri
# Date: 10/5/21
# Programming Assignment: 1
# Program Inputs: The length, width, and height of a room in feet.
# Program Outputs: The area and the amount of paint and primer needed to cover the room.

import math

#initialize variables
width_wall = 0.0
length_wall = 0.0
height_wall = 0.0

print("\nPaint your room! Enter the dimensions of the room in feet.")

length_wall = float(input("\n\tEnter desired length:"))
width_wall = float(input("\n\tEnter desired width:" ))
height_wall = float(input("\n\tEnter desired height:" ))

#Calculate the area, gallons of primer & gallons of paint
area = (length_wall + width_wall) + 2 * ((length_wall * height_wall) + (width_wall * height_wall))
primer = math.ceil(area/200)
paint = math.ceil(area/350)

print("\nThe total area of the four walls and ceiling is", area, "feet.")
print("\nThe gallons of primer needed to coat the area is", primer, "gallons.")
print("\nThe gallons of paint needed to cover the area is", paint, "gallons.")