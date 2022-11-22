#TamarraJP1
#Programmer: Joshua Tamarra
#Email: jtamarra@cnm.edu
#Purpose: provides user capability to calculate volume of a pyramid.

import math

a = float(input("Base number: ")) #length

h = float(input("Height number: ")) #height

volume = a**2 * h/3 #Volume formula/equation

s  = math.sqrt((h**2 + (a/2)**2)) #Slant height formula/equation

side = s * a/2

print("\nSurface area: ")
print(format(side*4,".3f"))

print("\nVolume: ")
print(format(volume,".3f"))


