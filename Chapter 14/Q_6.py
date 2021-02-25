"""Write a class called Converter. The user will pass a length and a unit when declaring an
object from the class—for example, c = Converter(9,'inches'). The possible units are
inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. For each of these
units there should be a method that returns the length converted into those units. For example,
using the Converter object created above, the user could call c.feet() and should get
0.75 as the result."""

class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def convert(self, unit_convert):
        unit_list = ["inches", "feet", 'yards', 'miles', 'kilometers', 'meters', 'centimeters']
        value_on_foot = [12, 1, 1 / 3, 1 / 5280, 1 / 3281, 1 / 3, 30]
        if unit_convert in unit_list:
           length_convert = round(
                self.length * value_on_foot[unit_list.index(unit_convert)] / value_on_foot[unit_list.index(self.unit)],
                9)
        return "{1} {0}".format(length_convert, unit_convert)

    def inches(self):
        return self.convert('inches')

    def feet(self):
        return self.convert('feet')

    def yards(self):
        return self.convert('yards')

    def miles(self):
        return self.convert('miles')

    def kilometers(self):
        return self.convert('kilometers')

    def meters(self):
        return self.convert('meters')

    def centimeters(self):
        return self.convert('centimeters')


c = Converter(9, "inches")
print(c.yards())
print(c.miles())
