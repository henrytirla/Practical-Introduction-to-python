"""(a) Write a function called add_excitement that takes a list of strings and adds an exclamation
point (!) to the end of each string in the list. The program should modify the
original list and not return anything.
(b) Write the same function except that it should not modify the original list and should
instead return a new list."""


def add_exictement(x):

    x=[words + "!" for words in x]

def add_exictement2(x):
    new_c =[]
    for words in x:
        new_word =words + "!"
        new_c.append(new_word)
    return new_c




    
