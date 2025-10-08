# Basic string creation and indexes:
greeting = "Welcome"
name = "sir"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o

# 0 1 2
# S i r

second_letter = greeting[1]
# Gets the second character in the greeting

print(second_letter)
# Prints the second character in the greeting : "e"

message = greeting + " " + name + ". You're back home!"
# Puts together the greeting and name into a message

print("Concatenated message:", message)
# Prints concatenated message

word = "Super-cali-fragil-istic-expi-ali-docious"

print("First letter:", word[0])
# Prints the first character in the word

print("Last letter:", word[-1])
# Prints the last character in the word

print("Range of letters (non-inclusive):", word[3:7])
# Prints all characters from the word from 3 to 6 "per_c" as the last index is non-inclusive

print("Another Range of letters (non-inclusive):", word[:-1])
# Prints all characters from the word except the last one

print(word[:5])
# First 5 characters

print("Last seven letters:", word[-7:])
# Prints the last seven characters in the word

print("Step through every second character:", word[::2])
# Prints every second character in the word

print("Reversed Word:", word[::-1])
# Prints the word in reverse order

print("Reversed, stepping every third letter:", word[::-3])
# Prints the word in reverse order, stepping every third character


## Built in functions

country = "Pakistan"
length_of_word = len(country)
print(length_of_word)

country = "Finland"
length_of_word = len(country)
print(length_of_word)

phrase = "spOngEBOB"

print("\nUppercase:", phrase.upper())
# Prints the phrase in uppercase

print("Lowercase:", phrase.lower())
# Prints the phrase in lowercase

print("Capitalized:", phrase.capitalize())
# Prints the phrase with the first letter capitalized

print("Title Format:", phrase.title())
# Prints the phrase in title case

#Find and replace text
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
print(sentence)
print(new_sentence)

# FORMATTED STRINGS IN PYTHON
# f-strings allow variables and expressions inside strings

print("\n--- Formatted Strings ---")

name = "Azaan"
age = 14
city = "NJ"

print(f"Hello, my name is {name}. I am {age} years old and live in {city}.")
print(f"I'll be, {age + 1} next year. My name in uppercase is {name.upper()}")

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

quote = input("Enter your favorite quote (or any quote you want): ")
length = len(quote)
print(f"The quote, '{quote}', is {length} characters long")


# Challenge 2: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Output formatted name: Lovelace, Ada
f_name = input("Enter your first name: ")
s_name = input("Enter your last name: ")
Formatted_Name = f_name.capitalize() + ", " + s_name.capitalize()
print(Formatted_Name)

# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# Backwards: nohtyP

word = input("Enter a word: ")
uppercase = word.upper()
lowercase = word.lower()
backwords = word[::-1]
print(f"The word inputted: {word}. \n Here it is in uppercase: {uppercase}. \n Here it is in lowercase: {lowercase}. \n Here it is backwards: {backwords}")