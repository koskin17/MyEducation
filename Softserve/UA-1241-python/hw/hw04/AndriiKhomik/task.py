temperature = int(input("Enter the temperature in Celsius: "))
absolute_zero = -273.15
degree_sign = u'\N{DEGREE SIGN}'
if temperature > absolute_zero:
    to_fahrenheit = int((temperature * 9 / 5) + 32)
    print(f"{str(temperature)}{degree_sign}C is equivalent to {str(to_fahrenheit)}{degree_sign}F")
else:
    print(f"Temperature below absolute zero ( {str(absolute_zero)}{degree_sign}C)")