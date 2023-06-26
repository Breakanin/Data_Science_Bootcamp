menu = ('Coffee', 'Tea', 'Cake', 'Biscuit')

# Dictionary of stock
stock = {'Coffee': 20, 'Tea': 16, 'Cake': 10, 'Biscuit': 12}
items = stock.keys()
qualities = stock.values()

# Dictionary of prices
price = {'Coffee': 1.50, 'Tea': 1.00, 'Cake': 2.20, 'Biscuit': 0.80} 
items = stock.keys()
prices = stock.values()

# Calculating value of total stock
total_stock = 0
for items in menu:
    item_value = (stock[items] * price[items])
    total_stock += item_value
print("Total value of the stock is: " + str(total_stock))