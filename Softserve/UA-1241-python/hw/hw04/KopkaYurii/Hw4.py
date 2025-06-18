TempCel = float(input("Enter the temperarure in Celsius: "))
if TempCel < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
else:
    tempFar = (TempCel * 9/5) + 32
    print(f"{TempCel}°C is equivalent to {tempFar}F")
