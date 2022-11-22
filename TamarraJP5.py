#TamarraJP5
#Programmer: Joshua Tamarra
#Email: jtamarra@cnm.edu
#Purpose: Demonstrates use of functions
from math import sin, cos, sqrt, atan2

print("Hello, here to calculate some distances? I gotchu bro\n")

# Earth's radius
r = 6371.0

# Functions
def header():
    print("In this program, you will be entering two location's latitudes and longitudes.")

def get_location():
    lat = float(input("Enter the latitude (In decimal degrees): "))
    lon = float(input("Enter the longitude (In decimal degrees): "))
    return (lat, lon)

def calcDistance(p1, p2):
    a = sin((p2[0]-p1[0])/2)**2 + cos(p1[0]) * cos(p2[0]) * sin((p2[1]-p1[1])/2)**2
    #c = 2 * atan2( √a, √(1−a) )
    c = 2*atan2(sqrt(a),sqrt(1-a))
    d = r * c
    return d*1.852

# MAIN #
header()

while True:
    loc1 = get_location()
    print(loc1)
    loc2 = get_location()
    print(loc2)

##ABQ    lat1 = 35.6870
##ABQ    lon1 = 105.9378
##STA FE lat2 = 35.0844
##STA FE lon2 = 106.6504

    distance = calcDistance(loc1, loc2)
    
    print(distance)

    doAnother = input("Would you like to calculate another? (y/n) ").lower()
    
    if doAnother == "y":
        continue
    else:
        break
