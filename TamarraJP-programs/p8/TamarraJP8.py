#TamarraJP8
#Programmer: Joshua Tamarra
#Email: jtamarra@cnm.edu
#Purpose: demonstrates how to define a class further

from GeoPoint import *

##  MAIN  ##
while True:
    point1 = GeoPoint(36.7783,119.4179,"California")
    point2 = GeoPoint()
    point2.point = (40.7128,74.0060)
    point2.desc = "New York"
    userlat = float(input("Enter your latitude: "))
    userlon = float(input("Enter your longitude: "))
    pointUser = GeoPoint(userlat,userlon, 'User Location')
    distanceToOne = point1.CalcDistance(pointUser)
    distanceToTwo = point2.CalcDistance(pointUser)
    CalculatePoint1 = point1.CalcDistance(pointUser) # Calculating point1's self.lat/lon and the users lat/lon
    CalculatePoint2 = point2.CalcDistance(pointUser)

    if CalculatePoint1 < CalculatePoint2:
        print(f"You are the closests to {point1.GetDescription()} which is located at {point1.GetPoint()[0]} and {point1.GetPoint()[1]}")
    elif CalculatePoint2 < CalculatePoint1:
        print(f"You are the closests to {point2.GetDescription()} which is located at {point2.GetPoint()[0]} and {point2.GetPoint()[1]}")

    doAnother = input("Would you like to calculate another? (y/n) ").lower()
    if doAnother == "y":
        continue
    else:
        break