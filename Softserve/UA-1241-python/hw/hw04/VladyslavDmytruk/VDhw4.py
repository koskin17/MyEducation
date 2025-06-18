def convert(celsius):
    if celsius < -273.15:
        print("Error: Temperature below (-273.15°C)")
    elif celsius > -273.15:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equivalent to {fahrenheit}°F")
try:
    celsius_input = float(input("Set the temperature in Celsius: "))
    convert(celsius_input)
except:
    print("Error: The temperature is set in Celsius. Use the numbers")
