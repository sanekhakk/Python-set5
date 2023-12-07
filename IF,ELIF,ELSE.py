#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     14-09-2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


str1=input("M or F: ")
age=int(input("age: "))
if((str1=='M') & (age>=65)):
    print("Eligible for concession")
elif((str=='F') & (age>=60)):
    print("Eligible for concession")
else:
    print("Not eligible for concession")