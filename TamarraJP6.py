#TamarraJP5
#Programmer: Joshua Tamarra
#Email: jtamarra@cnm.edu
#Purpose: demonstrates how to define a class with your geo point functions

from math import sin, cos, sqrt, atan2

class GeoPoint():
    # Defining the variables right away and initiate the parameters as 0
    def __init__(self, lat=0, lon=0, description=""):
        self.lat = lat
        self.lon = lon
        self.description = description

    # Setting up the point that when called outside the class
    def SetPoint(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # Calling that point, so you can retrieve the tuple
    def GetPoint(self):
        return (self.lat, self.lon)

     # Calculation
    def CalcDistance(self, lat, lon): 
        r = 6371.0
        a = sin((self.lat-lat)/2)**2 + cos(lat) * cos(self.lat) * sin((self.lon-lon)/2)**2
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

## MAIN ##

#loop
while True:
    userlat1 = float(input("First location's latitude: "))
    userlon1 = float(input("First location's longitude: "))
    userlat2 = float(input("Second location's latitude: "))
    userlon2 = float(input("Second location's longitude: "))

    point1 = GeoPoint()
    point2 = GeoPoint()

    point1.SetDescription("California")
    point1.SetPoint(36.7783,119.4179) # Setting the default
    print()
    print(point1.GetDescription(),"\n----------\n",point1.GetPoint(),"\n")

    point2.SetDescription("Denver")
    point2.SetPoint(39.7392,104.9903)
    print()
    print(point2.GetDescription(),"\n----------\n",point2.GetPoint(),"\n")
    
    CalculatePoint1 = point1.CalcDistance(userlat1, userlon1) # Calculating point1's self.lat/lon and the users lat/lon
    CalculatePoint2 = point2.CalcDistance(userlat2, userlon2) # Calculating point2's self.lat/lon and the users lat/lon 
    
    # !!You are closest to <description> which is located at <point’s lat and lon coordinates>

    if CalculatePoint1 < CalculatePoint2:
        print(f"You are the closests to {point1.GetDescription()} which is located at {point1.GetPoint()[0]} and {point1.GetPoint()[1]}")
    elif CalculatePoint2 < CalculatePoint1:
        print(f"You are the closests to {point2.GetDescription()} which is located at {point2.GetPoint()[0]} and {point2.GetPoint()[1]}")

    doAnother = input("Would you like to calculate another? (y/n) ").lower()
    if doAnother == "y":
        continue
    else:
        break

