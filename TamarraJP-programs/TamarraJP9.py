# TamarraJP9
# Programmer: Joshua Tamarra
# Email: jtamarra@cnm.edu
# Purpose: demonstrates how to define a class with a file input

from math import sin, cos, sqrt, atan2, radians
import os

class GeoPoint():
    # Defining the variables right away and initiate the parameters as 0
    def __init__(self, lat=0.0, lon=0.0, description=""):
        self.lat = lat
        self.lon = lon
        self.description = description

    # Setting up the point that when called outside the class
    def SetPoint(self, point):
        self.lat = point[0]
        self.lon = point[1]

    # Calling that point, so you can retrieve the tuple
    def GetPoint(self):
        return (self.lat, self.lon)

     # Calculation
    def CalcDistance(self, point): 
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(point.lat)
        lon2 = radians(point.lon)

        r = 6371.0
        a = sin((lat1-lat2)/2)**2 + cos(lat2) * cos(lat1) * sin((lon1-lon2)/2)**2
        #c = 2 * atan2( √a, √(1−a) )
        c = 2*atan2(sqrt(a),sqrt(1-a))
        d = r * c
        return d*1.852

    # Setting up that description
    def SetDescription(self, description):
        self.description = description

    # Calling that description
    def GetDescription(self):
        return self.description

    point = property(GetPoint, SetPoint)
    desc = property(GetDescription, SetDescription)


##  MAIN  ##
while True: 
    pointsList = []
    # print(os.listdir())
    try:
        with open("Points.txt", "r") as f:
            for i in f.readlines():
                print (i)
                line = i.split(",")
                pointsList.append(line)
                
            print(pointsList)
    except: 
        print("There was an error, are you in the right file path?")

    userlat = float(input("Enter your latitude: "))
    userlon = float(input("Enter your longitude: "))
    pointUser = GeoPoint(userlat,userlon, 'User Location')
    newPoint = GeoPoint(pointsList)
    CalculatePoint = newPoint.CalcDistance(pointUser)

    doAnother = input("Would you like to calculate another? (y/n) ").lower()
    if doAnother == "y":
        continue
    else:
        break
