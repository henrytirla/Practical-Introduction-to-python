"""Write a program that asks the user to enter a password. If the user enters the right password,
the program should tell them they are logged in to the system. Otherwise, the program
should ask them to reenter the password. The user should only get five tries to enter the
password, after which point the program should tell them that they are kicked off of the
system."""

numberoftries = 0

while numberoftries < 5:
    rightpass ="henry"
    askuserpass=input("Enter Password: ")

    if askuserpass == rightpass:
        print("User Access Granted")
        numberoftries += 1
        break
    else:
        numberoftries += 1
        print("Wrong Password","Number of tries left",5-numberoftries)


