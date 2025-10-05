# Python libraries are repositories of code.
# To import a library, type "import" followed by the library name.

import math  # Importing the math library
print("\n-- Math Library --")  # Print a section header
print("Square Root: ", math.sqrt(14))  # Print the square root of 14
print("Round Up: ", math.ceil(1.4))  # Print the ceiling of 1.4
print("Round Down: ", math.floor(1.4))  # Print the floor of 1.4
print("Power: ", math.pow(12, 12))  # Print 12 to the power of 12
print("Pi Value: ", math.pi)  # Print the value of pi



# Random

import random
random_int = random.randint(10000, 99999)
random_index = random.randint(1, 5)
random_int_table = []
for i in range(5):
    random_int_table.append(random_int)
    random_int = random.randint(10000, 99999)
    print(random_int_table)
chosenseed = random_int_table[random_index]
print("Chosen Seed:", chosenseed)

while not (1 < chosenseed < 10):
    random_div = random.randint(2, 5) 
    random_mult = random.randint(1, 2)
    chosenseed = (chosenseed / random_div) * random_mult

chosenseed = math.floor(chosenseed)
print("Final Key:", chosenseed)