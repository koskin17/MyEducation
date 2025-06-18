def convert(temperature):
    print(f"{temperature}*C is equivalent to {(temperature*9/5)+32}*F" if temperature > -273.15 else "Temperature below absolute zero (-273.15*C)")
convert(temperature = float(input("Enter the temperature in Celsius: ")))