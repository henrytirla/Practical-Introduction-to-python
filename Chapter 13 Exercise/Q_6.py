"""Write a function called binom that takes two integers n and k and returns the binomial coefficient
  n!
k!(n􀀀k)! ."""


def binomialCoeff(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # Recursive Call
    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)


print(binomialCoeff(5,2))

#credit https://www.geeksforgeeks.org/binomial-coefficient-dp-9/