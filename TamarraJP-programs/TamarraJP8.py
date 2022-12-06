#TamarraJP8
#Programmer: Joshua Tamarra
#Email: jtamarra@cnm.edu
#Purpose: demonstrates how to define a class further

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
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(point.lat)
        lon2 = radians(point.lon)

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

    point = property(GetPoint, SetPoint)
    desc = property(GetDescription, SetDescription)


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
    CalculatePoint1 = point1.CalcDistance(userlat, userlon) # Calculating point1's self.lat/lon and the users lat/lon
    CalculatePoint2 = point2.CalcDistance(userlat, userlon)

    if CalculatePoint1 < CalculatePoint2:
        print(f"You are the closests to {point1.GetDescription()} which is located at {point1.GetPoint()[0]} and {point1.GetPoint()[1]}")
    elif CalculatePoint2 < CalculatePoint1:
        print(f"You are the closests to {point2.GetDescription()} which is located at {point2.GetPoint()[0]} and {point2.GetPoint()[1]}")

    doAnother = input("Would you like to calculate another? (y/n) ").lower()
    if doAnother == "y":
        continue
    else:
        break