""""Write a class called Password_manager. The class should have a list called old_passwords
that holds all of the user’s past passwords. The last item of the list is the user’s current password.
There should be a method called get_password that returns the current password
and a method called set_password that sets the user’s password. The set_password
method should only change the password if the attempted password is different from all
the user’s past passwords. Finally, create a method called is_correct that receives a string
and returns a boolean True or False depending on whether the string is equal to the current
password or not."""

class Password_manager:
    def __init__(self, old_passwords):
        self.old_passwords = paswords



    def get_password(self):
        return paswords[-1]

    def set_password(self):
        new_pass =(input("Enter Your New Pass: " ))
        if new_pass in paswords:
            return "Password found in list,Choose new pass"
        else:
            paswords.append(new_pass)
            return "New Password is Set",paswords[-1]




    def is_correct(self,string):
        if string == self.old_passwords[-1]:
            return True
        else:
            return False


paswords= ["Henry","Gaga","Nelson"]
a  = Password_manager(paswords)

#print(a.get_password())
#print(a.set_password())
print(a.is_correct("Nelson"))






