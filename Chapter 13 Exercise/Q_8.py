"""Write a function called number_of_factors that takes an integer and returns how many
factors the number has."""

def factors_num(n):
    count = 0
    for  num in range(1,n):
         if n % num ==0:
            count += 1
    print(count)


factors_num(28)