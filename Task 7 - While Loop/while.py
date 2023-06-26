total = 0
number_of_inputs = 0

# I'm asking a user to enter the number
user_input = int(input("Please enter the number (-1 to exit): "))

# While loop to calculate the sum and number of times a user enter the input
# to later be able to calcuate average
while user_input != -1:
    total += user_input
    number_of_inputs += 1
    user_input = int(input("Please enter the number (-1 to exit): "))

    # If user enter -1 the while loop will break and print the average
    if user_input == -1:
        average = total / number_of_inputs
        # print(total)
        # print(number_of_inputs)
        print("Average of user inputs are: " + str(average))
        break