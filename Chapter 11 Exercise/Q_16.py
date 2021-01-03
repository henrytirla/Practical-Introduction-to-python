"""(a) Write a program that converts Roman numerals into ordinary numbers. Here are the
conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things
like IV being 4 and XL being 40.
(b) Write a program that converts ordinary numbers into Roman numerals"""

roman_literal={1 :"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV",15:"XV",
               16:"XVI",17:"XVII",18:"XVIII",19:"XIX",20:"XX",50:"L",100:"C",500:"D",1000:"M"}


# def roman_Covert(x):
#
#     num_string= str(x)
#     res = [int(x) for x in str(x)]
#
#     for key ,val in roman_literal.items():
#         if x == key:
#            print(roman_literal[key])
#         if x > key and x < key:
#             print(key)
#
#
#
# print(roman_Covert(20))

           #return roman_literal[key]


def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise (TypeError,"expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise (ValueError, "Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
        #print(result,"result")
        #print(input,"Input")
    return ''.join(result)


print(int_to_roman(22))
