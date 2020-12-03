"""Create a 5 X 5 list of numbers. Then write a program that creates a dictionary whose keys are
the numbers and whose values are the how many times the number occurs. Then print the
three most common numbers."""

matrix_5= [1,2,3,4,5,
           5,6,7,4,5,
           6,7,8,0,3,
           4,2,1,5,6,
           7,8,9,0,5]

def creatList():
    matrix_dict={}
    for num in range(len(matrix_5)):
        key = matrix_5[num]
        value = matrix_5.count(key)
        matrix_dict.update({key:value})
    return matrix_dict



print(creatList())




