# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

print("Functions (Procedures)")

print("\nExample 1")

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi()
say_bye()
say_hi()

print("\nExample 2")

def express_this(e):
    return e #e is a parameter

expression = express_this(1+2) # the mathmatical expression is hte argument
print(expression)
expression2 = express_this(45 * 6)
print(expression2)

print("\nExample 3")

def greeter(n): #n is the parameter
    return f"Hi {n}!"

first = greeter("Gojo")
second = greeter("Toji")
third = greeter("Sukuna")

print(first, second, third)

print("\nExample 4")

def remainder(a,b):
    return a % b

result = remainder(11, 111)
print(result)

print("\nExample 5")

def is_far(distance):
    # INSERT BASE CASE
    if distance < 1:
        return "error"
    if distance >= 100:
        return "That's far!"
    elif distance < 100 and distance >= 20:
        return "That's not that far!"
    elif distance < 20:
        return "That's near!"
    
print(is_far(-400))


def double_sequencer(number, times):
    value = number
    sequence = []
    for i in range(times):
        value = value * 2
        sequence.append(value)
    return sequence

result = double_sequencer(1, 5)
print(result)
