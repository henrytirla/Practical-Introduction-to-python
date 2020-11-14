"""An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
tells them if it is squarefree or not."""

from math import sqrt
def squareFree(num):
    #for num in range(1,n):
        divisors = []
        results = 0
        square_num = []

        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
                results = sum(divisors)
        for j in range(len(divisors)):
            while  divisors[j] != 1  and divisors[j] % sqrt(divisors[j]) == 0  :
                #sq =num / divisors[j] != 0
                if num % divisors[j] == 0:
                   square_num.append(divisors[j])
                   return(num,"SQUARES FOUND,Its Squares are",square_num,divisors)
                else :
                   return (num,"Is not a square",divisors)

##When No ssquare is found none is returned .##This is a bug im still to fix

print(squareFree(49))