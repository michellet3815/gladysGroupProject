import io
import json

"""
    Student: Nhi Pham
    Module: gladysSatellite
    Description: This module reads satellite data from a json file and finds a matching x, y to return the value.
"""

# start of code by Nhi Pham
def readSat(sat, pathToJSONDataFiles):
    """
        reads satellite data from a json file
        Students do NOT need to change the readSAT function
    """

    # data file path
    fileName = sat + "-satellite.json"
    filePath = pathToJSONDataFiles + "/" + fileName

    # open the file
    try:
        fileHandle = open(filePath)
    except IOError:
        print("ERROR: Unable to open the file " + filePath)
        raise IOError

    # print ("filePath = ", filePath)

    # read the file
    data = json.load(fileHandle)

    return data


def gpsValue(x, y, sat):
    value = 0

    pathToJSONDataFiles = './gladysData'
    data = readSat(sat, pathToJSONDataFiles)

    for record in data:
        if record["x"] == x and record["y"] == y:
            value = record["value"]

    return value
# end of code by Nhi Pham