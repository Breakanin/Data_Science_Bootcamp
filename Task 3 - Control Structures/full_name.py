# Ask the user to input their full name.

full_name = input("Please enter your full name: ")

# Perform some validation to check that the user has entered a full name.
# This program will be used to validate that a user inputs
# at least two names when asked to enter their full name.

name_surname = full_name.split()
len(name_surname) >= 2   # some people have double name or double surname

# Give an appropriate error message if they haven’t.
# One of the following messages should be displayed based on the user’s input:
# o "You haven’t entered anything. Please enter your full name."

if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")

# o "You have entered less than 4 characters.
# Please make sure that you have entered your name and surname."

elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

# o "You have entered more than 25 characters.
# Please make sure that you have only entered your full name."

elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# o “Thank you for entering your name.”

elif len(name_surname) >= 2 and len(full_name) <= 25:
    print("Thank you for entering your name.")

else:
    print("Did you enter your full name and surname?")  # I'm not sure if I have to use "Else" if "Elif" did the job?