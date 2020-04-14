"""Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound."""

## 1kg = 2.20462 Pounds
## 1/10 meaning pound is rounded to one decimal number

weight_kg = eval(input("Enter Your Weights in Kg: "))

kg_to_pound = round(weight_kg * 2.20462,1)

print("Your Weight in Pounds is :",kg_to_pound)