"""Using the dictionary created in the previous problem, allow the user to enter a dollar amount
and print out all the products whose price is less than that amount."""




my_dict ={'Mercedez': '100','Ferrari':'200','Bugatti':'300'}
print(my_dict)

amt =eval(input("Enter Amount: $$"))
for key ,values in my_dict.items():
    if  int(values) < amt:
        print (key ,"->",values)


