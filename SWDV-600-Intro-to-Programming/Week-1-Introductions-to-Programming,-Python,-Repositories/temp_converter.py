for i in range(3):
    tempCels = float(input("Enter the temperature in Celsius:"))
    print("Temperature in Fahrenheit:", str(float(tempCels*9/5+32)))

for i in range(3):
    tempFahr = float(input("Enter the temperature in Fahrenheit:"))
    print("Temperature in Celsius:", str(float((tempFahr-32)*5/9)))
