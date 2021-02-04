"""

Write a function called rectangle that takes two integers m and n as arguments and prints
out an mx n box consisting of asterisks. Shown below is the output of rectangle(2,4)
****
****

"""

def rectangle(m,n):
    for i in range(0,m):
        out = n * "*"
        print(out)
    



rectangle(2,4)
