""" Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be. [Hint: print('*'*10) prints ten asterisks.]  """

n=eval(input("Enter a number to specify how high you want your box: "))

for i in range(10):
    print("*"*n) #Changing this parameter increases the size


