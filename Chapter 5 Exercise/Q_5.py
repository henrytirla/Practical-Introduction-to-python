"""  Write a program that asks the user to enter a number and prints the sum of the divisors of
that number. The sum of the divisors of a number is an important function in number theory."""

def sumDivisors(x):
   a = []
   for i in range(1,x):
       if x % i == 0:
           a.append(i)
   return a,"With Sum",sum(a)


x = int(input("Enter X:"))
print(sumDivisors(x))

