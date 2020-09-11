# Using a for loop, create the list below, which consists of ones separated by increasingly many
# zeroes. The last two ones in the list should be separated by ten zeroes.
# [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

# Initialising for the sequence start

num_list =[1]
for i in range(11):
    num_list = num_list + (i * [0]) + [1]


print(num_list)