'''3. Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.'''

feet = float(input("Enter the length in feet: "))

#we use match case instead on switch case
conversions = [
        ("inches", 12),  # 1 foot = 12 inches
        ("yards", 1/3),  # 1 foot = 1/3 yard
        ("miles", 1/5280),  # 1 foot = 1/5280 miles
        ("millimeters", 304.8),  # 1 foot = 304.8 millimeters
        ("centimeters", 30.48),  # 1 foot = 30.48 centimeters
        ("meters", 0.3048),  # 1 foot = 0.3048 meters
        ("kilometers", 0.0003048)  # 1 foot = 0.0003048 kilometers
        ]

# Display conversion options
print("1. Inches\n2. Yards\n3. Miles\n4. Millimeters\n5. Centimeters\n6. Meters\n7. Kilometers")

#input user choice
choice = int(input("Enter the number corresponding to the conversion you want: "))

print(f"{feet} feet is equal to {float(feet)*conversions[choice-1][1]}")