try:
    tempr = float(input("Enter the temperature in Celsius: "))
    if tempr >= -273.15:
        print(f"{tempr}°C is equivalent to {round((tempr * 9 / 5) + 32, 2)}°F")
    elif tempr < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
except:
    print("Error: Wrong value input")