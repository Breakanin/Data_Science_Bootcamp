# Design a program that determines the award
# a person competing in a triathlon will receive.
# My program should read in the times (in minutes) [I need an integer]
# for all three events of a triathlon, namely swimming, cycling, and running,
# triathlon = [swimming, cycling, running]

# swimming

swimming = (input("Please enter your time in swimming: "))
print("Your time in the swimming category is : " + swimming + " minutes")

# cycling

cycling = (input("Please enter your time in cycling: "))
print("Your time in the cycling category is : " + cycling + " minutes")

# running

running = (input("Please enter your time in running: "))
print("Your time in the running category is : " + running + " minutes")

# calculate and display the total time taken to complete the triathlon.

total_time = int(swimming) + int(cycling) + int(running)
print("Your Triathlon total time is: " + str(total_time))

# The award is based on the total time taken to complete the triathlon.
# The qualifying time for awards is 100 minutes.
# qualifying time == 100

# Display the award based on the following criteria:

# Within qualifying time. Provincial Colours

if total_time <= 100:
    print("Congratulations! You receive 'Provincial Colours Award'")

# Within 5 minutes of qualifying time. Provincial Half Colours

elif total_time <= 105:
    print("Congratulations! You receive 'Provincial Half Colours Award'")

# Within 10 minutes of qualifying time. Provincial Scroll

elif total_time <= 110:
    print("Congratulations! You receive 'Provincial Scroll Award'")

# More than 10 minutes of qualifying time. No award

else:
    print("Unfortunately you haven't finish within qualifying time. Try again next year.")