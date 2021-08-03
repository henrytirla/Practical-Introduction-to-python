"""Write a class called Investment with fields called principal and interest. The constructor
should set the values of those fields. There should be a method called value_after that
returns the value of the investment after n years. The formula for this is p(1 + i)n, where p is
the principal, and i is the interest rate. It should also use the special method __str__ so that
printing the object will result in something like below:
Principal - $1000.00, Interest rate - 5.12%"""


class Investment:
      def __init__(self,principal,interest,n):
          self.principal = principal
          self.interest = interest
          self.n = n

      def value_after(self):

          return_investment = self.principal*(1+self.interest)**self.n
          return return_investment

      def __str__(self):
          return ("Principal --$", self.principal,"Interest rate---", self.interest,"%","Interst $",a.value_after())




a = Investment(1000,5.12,3)
print((a.__str__()))
