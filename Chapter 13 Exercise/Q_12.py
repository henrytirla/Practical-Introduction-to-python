"""Recall that if s is a string, then s.find('a') will find the location of the first a in s. The
problem is that it does not find the location of every a. Write a function called find all that
given a string and a single character, returns a list containing all of the locations of that character
in the string. It should return an empty list if there are no occurrences of the character
in the string."""
import re
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


print(list(find_all("Henrye","e")))