# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
print("Welcome to the testing factory!")
print("This is test 1.")
num = int(input("Please enter a number to be tested."))
print("Testing...")
if num % 2 == 0: 
    print("Testing results: Even.")
else:
    print("Testing results: Odd.")



# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
print("This is test 2.")
day = input("Please enter a day of the week to be tested. Use only lowercase letters, otherwise testing may be inaccurate: ")
print("Testing...")

if day == "saturday" or day == "sunday":
    print("Testing results: Weekend.")
else:
    print("Testing results: Weekday.")


# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
print("This is test 3.")
import random

number = random.randint(1, 10)
guess = int(input(" In this test, you will try to guess a number between 1 and 10. Please enter a number between 1 and 10. "))

print("Testing..")

if guess == number:
    print("Testing results: Correct")
else:
    print("Testing results: Try again")



# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
print("This is test 4.")

num = int(input(" Please enter a positive integer: "))

print("Testing...")

if num % 2 == 0 and num > 10:
    print("Testing results: Big even number")
else:
    print("Testing results: Number does not meet criteria")



# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
print("This is the final test, test 5.")

num1 = int(input("Please enter a number to be tested: "))
num2 = int(input("This test requires two numbers. Please enter another number to be tested: "))

print("Testing...")

if num1 > num2:
    print("Testing results:",num1, "is larger.")
elif num2 > num1:
    print("Testing results:",num2, "is larger.")
else:
    print("Testing results: Numbers are equal.")

print("Thank you for visiting the testing factory! We hope you had a wonderful time! Use code KDHEU937432 to save 20% off on your next visit!")




