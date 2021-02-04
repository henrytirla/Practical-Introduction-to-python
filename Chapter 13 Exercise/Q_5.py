"""Write a function called first_diff that is given two strings and returns the first location in
which the strings differ. If the strings are identical, it should return -1."""

def first_diff(x,y):
    if len(x) == len(y):
        for i in range(1,len(x) + 1):
            if x[:] == y[:]:
                print("-1")
            elif x[:i] != y[:i]:
                print("They differ at the ",i, "Character",x[:i],y[:i])
                break
    else:
        print("These are non identical Strings")



first_diff("h2nry","henry")