# Challanges
print("\n Challange 1")

print("\n AP Pseudocode")
# PROCEDURE add(num1, num2)
#     {
#         sum <-- num1 + num2
#         RETURN(sum)
#     }
# DISPLAY(add(1, 10000))

# PROCEDURE subtract(num1, num2)
#     {
#         difference <-- num1 * num2
#         RETURN(difference)
#     }
# DISPLAY(subtract(1, 10000))

# PROCEDURE multiply(num1, num2)
#     {
#         product <-- num1 * num2
#         RETURN(product)
#     }
# DISPLAY(multiply(1, 10000))

# PROCEDURE divide(num1, num2)
#     {
#         quotient <-- num1 * num2
#         RETURN(quotient)
#     }
# DISPLAY(divide(1, 10000))

print("\n Python")

def add(num1, num2):
    sum = num1 + num2
    return sum
print(add(1,10))

def subtract(num1, num2):
    sum = num1 - num2
    return sum
print(subtract(1,10))

def divide(num1, num2):
    sum = num1 / num2
    return sum
print(divide(1,10))

def multiply(num1, num2):
    sum = num1 * num2
    return sum
print(multiply(1,10))

print("\n Challange 2")

print("\n AP Pseudocode")

# PROCEDURE average(num1, num2, num3)
#     {
#         average <-- (num1 + num2 + num3) / 3
#         RETURN(average)
#     }
# DISPLAY(average(1, 10000, 1000))

print("\n Python")

def average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average

print(average(1,11, 111))

print("\n Challange 3")

print("\n AP Pseudocode")
# PROCEDURE is_even(num)
#     {
#         even_odd <--- ""
#         IF num MOD 2 = 1 
#             {
#                 even_odd = "odd"
#             }
#         else
#             {
#                 even_odd = "even"
#             }
#         return even_odd
#     }
# DISPLAY(is_even(1))

print("\n Python")

def is_even(num):
    even_odd = ""
    if num % 2 == 1:
        return 'odd'
    else:
        return "even"

print(is_even(11))