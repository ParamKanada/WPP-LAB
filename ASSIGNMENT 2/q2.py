'''Q2. Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a
product name and print the corresponding price or a message if the product is not in the
dictionary.'''

#to store the product and it's price
def get_product():

    product_prices = {}
    while True:
        product_name = input("Enter product name (type 'done' to exit this program): ")
        if product_name.lower()== 'done':
            break

        price= float(input("Enter price: "))  # Use float to allow decimal prices
        product_prices[product_name] = price

    return product_prices

#checks the price of user's input product
def check_price(product_list):
    while True:
        product_name = input("Enter product name to look up (or type 'done' to exit): ")
        if product_name.lower() == 'done':
            break

        if product_name in product_list:
            print(f"The price of {product_name} is Rs. {product_list[product_name]:.1f}")
        else:
            print(f"{product_name} not found")

product_list = get_product()

check_price(product_list)