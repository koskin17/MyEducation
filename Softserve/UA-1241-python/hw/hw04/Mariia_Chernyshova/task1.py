c = int(input("Enter the temperature in Celsius: ",))
if c > -273.15 :
    print(f"{c}°C is equivalent to {round(c*9/5+32)}°F")
else :
    print("Temperature below absolute zero(-273.15°C)")