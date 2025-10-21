# Challenge 1: Palindrome Checker
# Write an algorithm that takes a string and returns True if it's a palindrome (reads the same forward and backward), otherwise False.
palindrominput = input("Enter a word to check if it is a palindrome: ")
palindrominputreverse = palindrominput[::-1]
if palindrominput == palindrominputreverse:
    print("Inputted Word Was A Palindrome")
else:
    print("Inputted Word Was Not A Palindrome")


# Challenge 2: Domain from Email
# Write an algorithm that takes an email address through user input and returns the domain (everything after the @ symbol).
emailinput = input("Enter your email: ")
domainsymbol = emailinput.index("@") + 1
domain = emailinput[domainsymbol::]
print(domain)


# Challenge 3: First and Last Match
# Given a list of strings, return True if the target matches the last element in the list.
given_list = ["orange", "blueberry", "cherry"]
guess = input("Guess the last thing in the list: ")
if given_list[-1] == guess:
    print("YOU ARE CORRECT")
else:
    print("FAILURE")


# Challenge 4: Conditional Suffix Adder
# Write an algorithm that takes a string.
# If the string is at least 3 characters and doesn’t end with "ing", add "ing".


# If it does end with "ing", add "ly".


# If it's less than 3 characters, return it unchanged.

gemmestring = input("Input some random word: ")
if len(gemmestring) >= 3:
    if "ing" in gemmestring:
        gemmestring += "ly"
    elif "ing" not in gemmestring:
        gemmestring += "ing"
    else:
        print("Error")
print(gemmestring)