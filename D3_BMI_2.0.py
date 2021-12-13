# Geting height and weight fro the user input
height = input("Enter your height in cm: ")
weight = input("Enter your weight in kg: ")

# Calculating BMI
BMI = (float(weight) / (float(height)/100) ** 2)

# Cheking results and showing warning message
if BMI <= 18.5:
    print("You have an underweight")
elif BMI <= 25:
    print("You have a normal weight")
elif BMI <= 30:
    print("You have an owerweight")
elif BMI <= 35:
    print("You have an obese")
else:
    print("You have a clinically obese")