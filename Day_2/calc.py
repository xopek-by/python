# Geting height and weight fro the user input
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Calculating BMI
BMI = (float(weight) / float(height) ** 2)

# Cheking results and showing warning message
if BMI <= 18.5:
    print("Your BMI is " + str(round(BMI, 1)) + " its too low, you need start to eat more")
elif BMI >= 24.9:
    print("Your BMI is " + str(round(BMI, 1)) + " its too high, you need to control your diet")
else:
    print("Your BMI is " + str(round(BMI, 1)) + " its super, you are awesome")