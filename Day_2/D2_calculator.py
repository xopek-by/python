# Waiting for the two-digit number and writing it to numbers variable
numbers = input("Input two numbers\n")

while len(numbers) !=2:
    print("You need to input only 2 digit number")
    numbers = input("Input two numbers\n")
else:
# Subscripting first and second number
    first_number  = (numbers)[0]
    second_number = (numbers)[1]
# Printing the results of first + second nubmers, with data conversion and the "answer" message 
    print("The answer is " + str(int(first_number) + int(second_number)))