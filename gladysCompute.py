import io
import math
import gladysSatellite as satellite

"""
     Student: Lo Tuan
     Module: gladysCompute
     Description: This module computes the distance between the current position and the destination position.
"""


# start of code by Lo Tuan
def gpsAverage(x, y):
    """
    Calculate average gps value of latitude, longitude, altitude, and time
    """


    value = satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, "longitude") + satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "time")
    average = value / 4
    return average


def distance(current, destination):
    """
    Calculate difference of average gps values of current position and destination position
    """
    currentAverage = gpsAverage(current[0], current[1])
    destinationAverage = gpsAverage(destination[0], destination[1])
    distance = math.sqrt((currentAverage**2) + (destinationAverage**2))

    return distance
# end of code by Lo Tuan