"""Write a function called factors that takes an 
integer and returns a list of its factors."""

def factors(n):
    list_factors=[]
    for i in range(n):
        if i > 0 and n % i == 0 :
            list_factors.append(i)
    print(list_factors)        
            

factors(12)