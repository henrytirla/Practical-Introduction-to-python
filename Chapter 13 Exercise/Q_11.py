"""Write a function called matches that takes two strings as arguments and returns how many
matches there are between the strings. A match is where the two strings have the same character
at the same index. For instance, 'python' and 'path' match in the first, third, and
fourth characters, so the function should return 3."""

def matches(x,y):
    count = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                count += 1
    print(count)             
    
    
matches("python","path")    