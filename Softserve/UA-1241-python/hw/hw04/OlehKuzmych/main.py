# Temperature convertor

c = input("Enter the temperature in Celsius: ")
b = -273.15
if float(c) < b:
  print(f"Temperature below absolute zero ({b}\u2103 )")
else:
  f = float(c) * 9 / 5 + 32
  print(f"{str(c).rstrip('0').rstrip('.')}\u2103\
  is equivalent to {str(f).rstrip('0').rstrip('.')}\u2109")