temperature = float(input('Enter the temperature in Celsius:'))
if temperature <= -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
elif temperature > -273.15:
    temperature_F = (temperature * 9/5) + 32
    print (f'{temperature}°C is equivalent to {temperature_F}°F')