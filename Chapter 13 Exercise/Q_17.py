"""(a) Write a function called primes that is given a number n and returns a list of the first n
primes. Let the default value of n be 100.
(b) Modify the function above so that there is an optional argument called start that allows
the list to start at a value other than 2. The function should return the first n primes that
are greater than or equal to start. The default value of start should be 2."""


def primes(n=10):

    primes_l=[]
    for number in range(1, 10):
      if number >1:
          for i in range(2, number):

              if (number % i) == 0:
                  break
          else:
              primes_l.append(number)
    print(primes_l)


primes(10)