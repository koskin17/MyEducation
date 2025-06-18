temperature = int(input("Enter the temperature in Celsius: "))
if temperature < -273.15:
    print("Temperature entered is below the ablosute zero.")
else:
    print(str(temperature) + "°C is equavilent to " + str((temperature * 9/5) + 32) + "°F")