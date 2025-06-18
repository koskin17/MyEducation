C = int(input("The temerature in celsium: "))
F= (C*9/5)+32

if C > -273.15:

    print (f"{C}°C is equivalent {F}°F")

else:

    print ("Error Temperature below absolute zero (-273.15°C)")