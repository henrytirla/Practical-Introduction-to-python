"""For this problem, use the dictionary from the beginning of this chapter whose keys are month
names and whose values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days
are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month
(e) Modify the program from part (a) and the dictionary so that the user does not have to
know how to spell the month name exactly. That is, all they have to do is spell the first
three letters of the month name correctly.
"""
import operator

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

#a
user_input= input("Enter Name of a month: ")
#user_input = "March"
for key, values in year.items():
     if user_input == key:  #change equality sign to in to answer d
        print( values)
        #break


#b
sorted_year ={key:year[key] for key in sorted(year)}
print(sorted_year.keys())

#c
for keys,values in year.items():
    if int(values) == 31:

      print(keys)

#d
##can sort months by changing itemgetter
# variable to 0
sorted_bymonthdays = dict(sorted(year.items(),key= operator.itemgetter(1)))
print(sorted_bymonthdays)
