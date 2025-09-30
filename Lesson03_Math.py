#KEY CONCEPTS: Math Operators: +, -, *, /, //, %, **

add = 7 + 2
# Addition
print("Sum: ", add)

subtract = 7 - 2
# Subtraction
print("Difference: ", subtract)

multiply = 7 * 2
# Multiplication
print("Product: ", multiply)

float_divide = 8 / 2
# Ceiling Division | Rounds Up
print("Float Quotient: ", float_divide)

integer_divide = 8 // 3
# Floor Division | Rounds Down
print("Integer Quotient: ", integer_divide)

modulus = 7 % 2
# Returns the remainder of a division
print("Remainder: ", modulus)

exponent = 2 ** 3
# Exponentiation | Power
print("Exponent: ", exponent)

Result1 = (2 + 3) * 4
print("Result1: ", Result1)

Result2 = 2 ** 3 * 4
print("Result2: ", Result2)

Result3 = 20 / 5 * 2
print("Result3: ", Result3)

Result4 = 10 - 2 + 3
print("Result4: ", Result4)

Result5 = 5 + 2 ** 3 * (4-1)
print("Result5: ", Result5)

# Challanges

Rectangle_Dimensions = (8, 5)
Area = Rectangle_Dimensions[0] * Rectangle_Dimensions[1]
print(Area)

m = 3.14
r = 7
Circle_Calculation = m * r ** 2
print(Circle_Calculation)

Shopping_List = {
    "Book": 12.99,
    "Notebook": 3.50
}

calculation = (Shopping_List["Book"] * 3) * (Shopping_List["Notebook"] * 4)
print(calculation)

print(7.0 % 4.9)

number = int(input("Enter a number to check if it is even or odd: "))
checker = number % 2
if checker == 0:
    print("The number is even")
elif checker == 1:
    print("The number is odd")
else:
    print("Invalid input")