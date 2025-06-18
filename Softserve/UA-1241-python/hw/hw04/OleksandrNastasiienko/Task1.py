#Temperature Converter

temtC = float(input("Enter the temperature in Celsius: "))
if temtC >= -273.15:
    tempF = (temtC * 9/5) + 32
    print(f"{temtC}C is equivalent to {tempF}F")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")