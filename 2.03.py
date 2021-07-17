#Enzo Lobo,3/18/21, surface area and volume of Cube
#Enzo Lobo,3/18/21, surface area and volume of Cube

from math import *

print("Jack wants to know the surface area and volume  of a Cube. The surface area is 6 s2 and the volume is s3. What is s? What is the surface area and volume of the Cube?")
print(" ")

s = input('What is the value of s?')
print("The value of s is " + s )

print(" ")

surfaceArea = 6 * pow(int(s), 2)
print("The surface area of the Cube is " + str(surfaceArea ))

print(" ")

volume = pow(int(s), 3)
print("The volume of the cube is " + str(volume))