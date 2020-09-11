# Write a program that removes any repeated items from a list so that each item appears at most
# once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].


ls = [1,1,2,2,3,4,3,0,0]

a = []


for i in ls:
    if i  not in a:
        a.append(i)
        
        
print(a)
