"""Write a function called one_away that takes two strings and returns True if the strings are of
the same length and differ in exactly one letter, like bike/hike or water/wafer."""

"""
count = 0
if len(a) == len(b)
    for i in a:
        for j in b:
            if i != j:
            count += 1
       if count == 1:
       print(true)
        

"""

def one_way(a,b):
   u = zip(a,b)
   count =0
   if len(a) == len(b):
       for i , j in u:
           if i != j:
               count += 1
       if count == 1:
          print(True)
   else:
       print("Not the same length")

    
    
    
one_way("Henry","Henrxf")
    
    