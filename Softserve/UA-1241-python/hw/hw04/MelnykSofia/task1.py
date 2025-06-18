degree_C=float(input("Enter a temperature in Celsius:"))
if degree_C>-273.15:
    print("Temperature in Fahrenheit:", (degree_C*9/5)+32, "F")
else: 
    print("Temperature below absolute zero (-273.15°C)")