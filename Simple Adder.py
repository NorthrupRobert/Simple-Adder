#Read in two floats from user, then compute the sum of those two numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
sum = num1 + num2

#print(f"The sum of the two numbers is {sum}!")
print("The sum of {0} and {1} is {2}." .format(num1, num2, sum))