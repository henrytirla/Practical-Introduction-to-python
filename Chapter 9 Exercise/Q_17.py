

'''Ask the user to enter the numerator and denominator of a fraction, and the digit they want to
know. For instance, if the user enters a numerator of 1 and a denominator of 7 and wants to
know the 4th digit, your program should print out 8, because 17
= .142856... and 8 is the 4th
digit. One way to do this is to mimic the long division process you may have learned in grade
school. It can be done in about five lines using the // operator at one point in the program
'''


num = eval(input('Enter numerator: '))
denum = eval(input('Enter denumerator: '))  
digit = int(input('Enter the digit you want to know: '))
i = 0
l=[]
while i < digit+1:   
    result=num//denum 
    mod=num%denum
    num=mod*10
    l.append(str(result))
    i+=1
u=l[-1]    
#l.insert(1,'.')
#v = ''.join(l)
#print(v) ''' to print out all the digits'''
print(f'The digit is {u}' )

