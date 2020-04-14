"""  Write a program that asks the user to enter an angle in degrees and prints out the sine of that
angle.  """


from math import*
import  math

number = math.radians(eval(input("Enter Degree: ")))
# number = math.degrees(number)
print("The Sin of Number is : ", sin(number))
