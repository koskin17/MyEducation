temperature = float(input("Enter the temperature in Celsius: "))
if temperature < -273.15:
    print("Error:Temperature below absolute zero(-273.15°С)")
else:
    in_F = temperature * 9/5 + 32
    print(f"{temperature}°C is equivalent to {in_F}°F")

