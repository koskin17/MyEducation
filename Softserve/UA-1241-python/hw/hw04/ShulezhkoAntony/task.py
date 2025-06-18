def temperature_converter(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
if celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    fahrenheit = temperature_converter(celsius)
    print(f"The temperature is equivalent to: {fahrenheit}")