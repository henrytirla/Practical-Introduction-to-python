x=eval(input("Enter size of angle between -180 and 180 degrees: "))
##  modulo gives the remainder, so the positive value, must return itself, which requires addition to 360, while the negative angle returns a value less than 360
print("The equivalent of the angle on the range between 0 and 360 degrees is", (x+360)%360)
