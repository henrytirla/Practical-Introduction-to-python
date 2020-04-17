"""Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
• If the temperature is less than -273.15, print that the temperature is invalid because it is
below absolute zero.
• If it is exactly -273.15, print that the temperature is absolute 0.
• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
• If it is 0, print that the temperature is at the freezing point.
• If it is between 0 and 100, print that the temperature is in the normal range.
• If it is 100, print that the temperature is at the boiling point.
• If it is above 100, print that the temperature is above the boiling point."""


temp_celcuis = eval(input("Enter temperature in Celcuis: "))
absolute_zero = -273.15
if temp_celcuis < absolute_zero:
    print("Temperature is invalid and below freezing point")
elif temp_celcuis ==   absolute_zero:
    print("The temperature is absolute zero")
elif temp_celcuis <= 0 :
    print("Temperature is below freezing point")
elif temp_celcuis == 0:
    print("Temperatur is at freezing point")
elif temp_celcuis > 0 and temp_celcuis < 100:
    print("Temperature is in normal range")
elif temp_celcuis == 100:
    print("The temperature is at boiling point")
elif temp_celcuis > 100:
    print("The temperature is above boiling point")


