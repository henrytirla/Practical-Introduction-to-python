"""A number is called a perfect number if it is equal to the sum of all of its divisors, not including
the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6
and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4,
7, 14, 28 and 28 = 1 + 2 + 4 + 7 + 14. However, 15 is not a perfect number because its divisors
are 1, 3, 5, 15 and 15 6= 1 + 3 + 5. Write a program that finds all four of the perfect numbers
that are less than 10000."""



def perfectNum(x):
  for num in range(1,x):
   divisors = []
   results = 0
   perfect_num=[]
   not_prime=[]
   for i in range(1,num):
       if num % i == 0:
           divisors.append(i)
           results = sum(divisors)


   if results == num:
      perfect_num.append(results)
      print("divisors",divisors,"num",num,"SumDivisors",results,"Perfect NUm",perfect_num)

print(perfectNum(10000))















