x = float(input("Enter the temperature in Celsius: "))
if x > -273.15:
    print (f"{x}°C is equivalent to {x * 9/5 + 32}°F")
else:
    print('Error: Temperature below absolute zero (-273.15°C)')