# Geting height and weight fro the user input
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculating BMI
BMI = weight / height ** 2

# Cheking results and showing warning message
if BMI <= 18.5:
    print("Your BMI is " + str(round(BMI, 2)) + " its too low, you need start to eat more")
elif BMI >= 24.9:
    print("Your BMI is " + str(round(BMI, 2)) + " its too high, you need to control your diet")
else:
    print("Your BMI is " + str(round(BMI, 2)) + " its super, you are awesome")