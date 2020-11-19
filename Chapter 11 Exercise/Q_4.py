"""Write a program that uses a dictionary that contains ten user names and passwords. The
program should ask the user to enter their username and password. If the username is not in
the dictionary, the program should indicate that the person is not a valid user of the system. If
the username is in the dictionary, but the user does not enter the right password, the program
should say that the password is invalid. If the password is correct, then the program should
tell the user that they are now logged in to the system."""
user_dict ={"Henry":"1234","Thomas":"Larissa","Monique":"Gaga"}
def CheckUser_Pass(x,y):
    for keys ,values in user_dict.items():
        if keys == x  and y == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")



x = input("Enter Username: ")    
y = input("Enter Your Password ")
print(CheckUser_Pass(x,y))
