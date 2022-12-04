# TamarraJP7
# Programmer: Joshua Tamarra
# Email: jtamarra@cnm.edu
# Purpose: demonstrates how to use error handling with the geo point class

from math import sin, cos, sqrt, atan2, radians

class GeoPoint():
    # Defining the variables right away and initiate the parameters as 0
    def __init__(self, lat=0, lon=0, description=""):
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
        r = 6371.0
        # a = sin((self.lat-lat)/2)**2 + cos(lat) * cos(self.lat) * sin((self.lon-lon)/2)**2
        a = sin((self.lat-point[0])/2)**2 + cos(point[0]) * cos(self.lat) * sin((self.lon-point[1])/2)**2
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

    # making the property class: learn more here https://www.geeksforgeeks.org/python-property-function/
    point = property(GetPoint, SetPoint)
    desc = property(GetDescription, SetDescription)

## MAIN ##

#loop
# while True:
#     try:
# userlat1 = float(input("First location's latitude: "))
# userlon1 = float(input("First location's longitude: "))
# userlat2 = float(input("Second location's latitude: "))
# userlon2 = float(input("Second location's longitude: "))

point1 = GeoPoint()
point2 = GeoPoint()

point1.point = (36.7783, 119.4179)
point1.desc = "California"
point2.point = (39.7392,104.9903)
point2.desc = "Denver"

print(f"{point1.desc} | {point1.point[0]}, {point1.point[1]}")
print(f"{point2.desc} | {point2.point[0]}, {point2.point[1]}")

