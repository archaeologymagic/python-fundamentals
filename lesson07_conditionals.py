# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")
# Boolean refresher:
print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4)
print(4 > 5)

# if
num1 = 10 
if num1 == 10: 
    print("Your number is equal to 10")

num2 = 13
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")
else: 
    print("Your number is greater than 12")

#if elif else
temperature = 93
if temperature >= 80: 
    print("It's hot!")
elif temperature >= 60:
    print("It's nice.")
else:
    print("It's cold!")

print()
print("--- Comparing Values with if/elif/else ---")

x = 20
y = 20

if x == y: 
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y: 
    print("x is less than y")
else: 
    print("error")

# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 
age = 17
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

# Using 'or' and 'not'
print("--- Using 'or' --- ")
day = "Monday"

if day == "Saturday" or  day == "Sunday":
    print("It's the weekend!")
elif day is "Monday" or day is "Tuesday":
    print("It's Monday or Tuesday")
else:
    print("It's Wed,Thur, or Fri")

if day is not "Monday":
    print("It's not Monday")

# Challenge 1: Even or Odd
# Ask the user for a number, and tell them if it’s even or odd.
# Example output:
# Enter a number: 7
# 7 is odd.
# Hint: use modulus operator

input1 = int(input("Enter a number:"))
if input1 % 2 == 1:
    print("Number is odd")
else:
    print("Number is even")


# Challenge 2: Password Check
# Create a variable with a stored password
# Ask the user to enter a password. 
# If it matches the stored password, print "Access granted." Otherwise, "Access denied."
# Example output:
# Enter password: dolphin
# Access granted. Access denied.
# Enter password: swordfish
# Access granted.

password_stored = "coolboy"
password_input = input("Enter your password: ")
if password_input == password_stored:
    print("Access Granted")
else:
    print("Access Denied")


# Challenge 3: Grading System
# Ask the user for a numeric grade (0-100) and print a letter grade (A,B,C,D,F).
# Example output:
# Enter your grade: 81
# You earned an B.

num_grade = int(input("Enter a number grade from 0-100: "))
if num_grade >= 93:
    print("A")
elif num_grade >= 90:
    print("A-")
elif num_grade >= 87:
    print("B+")
elif num_grade >= 83:
    print("B")
elif num_grade >= 80:
    print("B-")
elif num_grade >= 77:
    print("C+")
elif num_grade >= 73:
    print("C")
elif num_grade >= 70:
    print("C-")
elif num_grade >= 67:
    print("D+")
elif num_grade >= 64:
    print("D")
else:
    print("F")