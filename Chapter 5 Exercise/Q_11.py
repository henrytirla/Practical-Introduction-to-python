def factorial(x):
  for i in range(1, x):
    x *= i
  print(f'Factorial is {x}.')
num = eval(input('Enter a number: '))
factorial(num)
