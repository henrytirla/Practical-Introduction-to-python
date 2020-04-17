"""Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over."""

credits_taken = eval(input("Emter the number of credit taken: "))

if credits_taken <= 23:
    print("You are a fresh man")
elif credits_taken >= 24 and credits_taken <= 53:
    print("You are a sophormore")
elif credits_taken >= 54 and credits_taken <= 83:
    print("You are a Junior")
elif credits_taken >= 84:
    print("Congrats You are a Senior")