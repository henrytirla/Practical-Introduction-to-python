"""Write a class called Product. The class should have fields called name, amount, and price,
holding the product’s name, the number of items of that product in stock, and the regular
price of the product. There should be a method get_price that receives the number of
items to be bought and returns a the cost of buying that many items, where the regular price

is charged for orders of less than 10 items, a 10% discount is applied for orders of between
10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
also be a method called make_purchase that receives the number of items to be bought and
decreases amount by that much.

"""

class Product:
    def __init__(self,name,amount ,price):
        self.name =name
        self.amount =amount
        self.price = price

    def get_price(self):
        return self.price * self.amount

    def make_purchase(self):
        if self.amount < 10:
            return "Discount Price", self.amount * self.price
        elif self.amount in range(9,100):
            return "Discount Price",self.amount * self.price-(self.price * 0.01)
        elif self.amount >= 100:
            return "Discount Price",self.amount * self.price - (self.price * 0.02)



shop =Product("Henry",15,99)

print(shop.make_purchase())