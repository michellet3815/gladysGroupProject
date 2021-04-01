import io

"""
Student: Michelle Tran
Module: gladysUserLogin
Description: This module logs the user in.
"""

#start of code by Michelle Tran
def login():
    emailAddress = ""
    password = ""
    while emailAddress == "":
        emailAddress = input("Enter email address: ")
        password = input("Enter password: ")

        if '@' not in emailAddress:
            print("ERROR: User login is not an email address")
            emailAddress = ""
        elif ".com" not in emailAddress:
            print("ERROR: User login is not an email address")
            emailAddress = ""
        else:
            break

    return emailAddress
# end of code by Michelle Tran