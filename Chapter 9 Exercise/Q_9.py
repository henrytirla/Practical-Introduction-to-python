'''A 4000-year old method to compute the square root of 5 is as follows: Start with an initial
guess, say 1. Then compute  (1+(5/1))/2=3
Next, take that 3 and replace the 1’s in the previous formula with 3’s . This gives(3+(5/3))/2 = 2.33.
Next replace the 3 in the previous formula with 2.33.
If you keep doing this process of computing the formula, getting a result, and plugging it back
in, the values will eventually get closer and closer to square root of 5. This method works 
for numbers other than 5. Write a program that asks the user for a number and uses this method 
to estimatethe square root of the number correct to within 10E-10. The estimate will be correct to within
10E-10 when the absolute value of the difference between consecutive values is less than 10E-10.
'''


num=eval(input("Enter number: "))
x=1 #you can set any initial value
method=((x+(num/x))/2)
diff= method-x

while diff != 1*10**(-10) :
    method=((x+(num/x))/2)
    diff=(method-x)        
    x=method
    
    if diff==0:#this is used because the computer aproximates to zero at 1*10**(-10).
        print(round (x,2))
        break
