"""Write a simple quote-of-the-day program.
The program should contain a list of quotes, and
when the user runs the program,
a randomly selected quote should be printed."""
import random
from random import randint
Quotes_list = ["To double your income and success, tripple your investment in personal Developent and professional mastery -Robin Sharma","Simplicity is the soul efficiency - Austin Freeman", "A journey of a thousand miles begins with a single step -Lao Tzu","Everything happens for a reason. It's okay if you don't know what that reason is yet -Unknown"]

len_list = len(Quotes_list)
num =random.randint(0,len_list-1)

print(Quotes_list[num])




