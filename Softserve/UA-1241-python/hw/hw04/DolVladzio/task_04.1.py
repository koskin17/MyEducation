#=============================
c_temperature = input("Enter the temperature in Celsius: ")
    
try:
    if int(c_temperature) < -237.15:
        print("Error...Temperature below absolute zero (-273.15)C")
        
    elif int(c_temperature) >= -273.15:    
    #_Convert celsius to fahrenheit
        f_temperature = (int(c_temperature) * ( 9 / 5 )) + 32
            
        print(f"{c_temperature}C is equivalent to {f_temperature}F")
        
except :
    print("Incorrect input!\nTry again")  
#=============================
