import io
import math

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
Student: 
Module: gladysUserLogin
Description: This module logs the user in.
"""
# start of code by Khuong Le
def runTests():
    """
        tests some module functions
    """

    print("running a few tests")

    average = compute.gpsAverage(4, 5)
    print("average of 4 & 5 = ", average)

    value = satellite.gpsValue(0, 0, "altitude")
    print("value of 0 & 0 in altitude = ", value)

    start = [1, 2]
    end = [3, 4]
    distance = compute.distance(start, end)
    print("distance between start [1, 2] and end [3, 4] = ", round(distance, 2))

    print("hello!")


def start():
    """
        logs the user in, and runs the app
    """

    userName = userLogin.login()
    runApp(userName)
def runApp(userName):
    """
    runs the app
    """

    current = [-1, -1]
    destination = [-1, -1]

    userQuit = False
    while (not userQuit):
        print("\n--- Gladys West Map App ---\n")
        print("user = " + userName)

        print("\ncurrent position     : x = ", current[0], " , y = ", current[1])
        print("destination position : x = ", destination[0], " , y = ", destination[1])
        print("distance             : ", round(compute.distance(current, destination), 2))

        # menu
        print("[c] to set current position")
        print("[d] to set destination position")
        print("[m] to map - which tells the distance")
        print("[t] to run module tests")
        print("[q] to quit")

        print("\n-- Welcome to the Gladys West Map App --")
        print("Type t to run tests or q to quit\n")

        # get first character of input
        userInput = input("Enter a command: ")
        lowerInput = userInput.lower()
        firstChar = lowerInput[0:1]

        # set current location
        if firstChar == 'c':
            current[0] = int(input("Enter a x position: "))
            current[1] = int(input("Enter a y position: "))
        # set destination position
        elif firstChar == 'd':
            destination[0] = int(input("Enter a x position: "))
            destination[1] = int(input("Enter a y position: "))
        # map - tells the distance
        elif firstChar == 'm':
        # quit
            print(compute.distance(current, destination))
        elif firstChar == 'q':
            userQuit = True
        # run some tests (this is part 1 of 2)
        elif firstChar == 't':
            runTests()
        else:
            print("ERROR: " + firstChar + " is not a valid command")

    print("\n")
    print("Thank you for using the Gladys West Map App!")
    print("\n")
start()
# end of code by Khuong Le