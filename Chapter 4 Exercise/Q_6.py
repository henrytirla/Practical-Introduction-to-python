"""A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost."""

item_tobuy = eval(input("How many items do you want to buy:"))

if item_tobuy < 10:
    print("Total price is: ", item_tobuy*10)

elif item_tobuy in range(10,100):
    print("Total price is:", item_tobuy*10)
elif item_tobuy >= 100:
    print("Total price is: ",item_tobuy*7 )
