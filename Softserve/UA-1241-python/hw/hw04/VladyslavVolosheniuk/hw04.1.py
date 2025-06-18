while True:
    user_input = input("Enter temperature in Celsius(or 'exit' to stop): ")
    if user_input.lower() == 'exit':
        print("Program terminated.")
        break
    try:
        C = float(user_input)
        if C < -273.15:
            print("Error: Temperature below absolute zero (-273.15°C)")
            continue  
        formula = (C * 9/5) + 32
        print(f"{user_input}°C is equivalent to {formula}°F")
    except ValueError:
        print("Please enter a valid integer.")