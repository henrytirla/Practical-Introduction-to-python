"""Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature
is in. Your program should convert the temperature to the other unit. The conversions
are F = 95
C + 32 and C = 59
(F 􀀀 32)."""
import sys
temperature = int(input("Enter Temperateture: "))
degree = input("What Units C or F :")

if degree == "F" :
    c = 5/9*(temperature-32)
    print("Your Temperature in Celcius is: ", c)
    
elif degree =="C":
    f= 9/5*temperature + 32
    print("Your temperature in Fahrenheit is: ", f)
    

elif degree != "C" and degree!= "F":
    print("You entered wrong Units")
    sys.exit()
    
    
    