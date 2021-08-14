"""Companies often try to personalize their offers to make them more attractive. One simple
way to do this is just to insert the person’s name at various places in the offer. Of course,
companies don’t manually type in every person’s name; everything is computer-generated.
Write a program that asks the user for their name and then generates an offer like the one
below. For simplicity’s sake, you may assume that the person’s first and last names are one
word each.
"""

first_name = input("Please Enter your First  name: ")
last_name = input("Please Enter your Last name: ")

message = f"Dear {first_name} {last_name} I am pleased to offer you our new Platinum " \
          f"Plus Rewards card at a special introductory APR of 47.99%. {first_name}, an offer" \
          f"like this does not come along every day, so I urge you to call now toll-free at 1-800-314-1592. We cannot " \
          f"offer such a lowrate for long, {first_name}, so call right away.".format(first_name=first_name,last_name=last_name)


print(message)