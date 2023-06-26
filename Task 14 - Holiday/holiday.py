# Program is made to calculate a user’s holiday cost
# including the plane cost, hotel cost, and car rental cost

# Here are definitions of function needed to calculate total cost
def hotel_cost(num_nights):
    return num_nights * price_per_night


def plane_cost(city_flight):
    if city_flight == "Paris":
        flight_cost = 200
    elif city_flight == "New York":
        flight_cost = 400
    elif city_flight == "Tokyo":
        flight_cost = 800
    return flight_cost


def car_rental(rent_cost):
    return rental_days * rent_cost


def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost(num_nights) + plane_cost(city_flight) 
    + car_rental(rent_cost)


# Ask user for an input
city_flight = input("Enter the city of your destination: either Paris, New York or Tokyo: ")

num_nights = int(input("Enter number of nights at the hotel: "))
price_per_night = 50

rental_days = int(input("Enter the number of days you will rent the car: "))
rent_cost = 30

# Calculate total cost of holiday trip
total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)
print(f"Total holiday cost is: {total_cost}")
