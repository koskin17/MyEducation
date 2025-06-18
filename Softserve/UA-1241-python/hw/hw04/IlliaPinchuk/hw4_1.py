ABSOLUTE_ZERO_CELSIUS = -273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_temperature_input():
    temp = input("Enter the temperature in Celsius: ")
    while not is_number(temp):
        print("Please enter a valid temperature in Celsius.")
        temp = input("Enter the temperature in Celsius: ")
    return float(temp)


temp = get_temperature_input()

if temp < ABSOLUTE_ZERO_CELSIUS:
    print(f"Error: Temperature below absolute zero ({ABSOLUTE_ZERO_CELSIUS}°C)")
else:
    fahrenheit = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equivalent to {fahrenheit}°F")
