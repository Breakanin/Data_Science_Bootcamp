import math

# create a program that allows the user
# to access two different financial calculators:
# an investment calculator and a home loan repayment calculator

investment = 1
bond = 2

print("You have a two options: ")
print("1. investment - to calculate the amount of interest you'll earn on your investment")
print("2. bond - to calculate the amount you'll have to pay on a home loan")

user_investment_choice = input("Please enter either option 1 for 'investment' or 2 for 'bond' from the menu above to proceed: ")

if user_investment_choice == "1":

    deposit = float(input("Please enter the amount of money you are depositing: "))  # 'P'

    interest_rate = float(input("Please enter the number of the interest rate: ").strip('%'))  # 'r'
    interest_rate = (interest_rate/100)

    number_of_years = float(input("Please enter the number of years you plan on investing: "))  # 't'

    interest = input("Please choose wheter you like a 'simple' or 'compound' interest?")

    # Depending on whether or not they typed “simple” or “compound”,
    # output the appropriate amount that they will get back after the given period,
    # at the specified interest rate. See below for the formula to be used:
    # A = P*(1 + r*t))

    if interest == "simple":
        interest = deposit*(1 + interest_rate * number_of_years)
        print(f"Your will recieve {interest} after {number_of_years} years.")

    # A = P * math.pow((1+r),t)

    elif interest == "compound":
        interest = deposit * math.pow((1+interest_rate), number_of_years)
        print(f"Your will recieve {interest} after {number_of_years} years.")

elif user_investment_choice == "2":

    value_of_the_house = int(input("Please enter a value of the house. (e.g. 100000): "))  # 'P'

    interest_rate = int(input("Please enter the interest rate.(e.g. 7): "))

    monthly_interest_rate = (interest_rate / 100) / 12  # 'i'

    number_of_months = int(input("Please enter the number of months they plan to take to repay the bond. (e.g. 120): "))  # 'n'

    repayment = (monthly_interest_rate * value_of_the_house)/(1 - (1 + monthly_interest_rate)**(- number_of_months))
    print(f"Your monthly bond repayment will be {repayment}")

# If the user doesn’t type in a valid input, show an appropriate error message.

else:
    print("Please enter either '1' or '2': ")