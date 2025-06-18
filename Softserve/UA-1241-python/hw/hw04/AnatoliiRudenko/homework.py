temperature=input("Enter temperature in Celcius: ")
temperature=float(temperature)
if temperature< -273.15:
    print("Error")
else:
    tempfahrenheit=(temperature*(9/5))+32
    print("Temperature in F is: "+ str(tempfahrenheit))
