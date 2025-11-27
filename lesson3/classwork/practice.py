# Problem 1
# Ask the user to enter their height in centimeters.
# Print "Tall" if the height is greater than 170, otherwise print "Short".

height = int(input("How tall are you in Centimeters?"))
if height > 170:
    print("You are a very very tall person, almost as tall as Lebron James! 67!")
elif height == 170:
    print("You are average height. Sorry.")
else:
    print("You are very short. like a Hobbit.")

# Problem 2
# Ask the user for their age.
# If they are 18 or older, print "Adult", else print "Minor".

age = int(input("How old are you?"))
if age == 67:
    print("YAYAYAYAYAYAAYYAAYAYAYAYAAYAYAYYAYAYAYAYAYAYAYAYYA!!!!")
elif age == 18:
    print("Congratulations! You're officially an Adult!")
elif age < 18:
    print("You are a baby. Ain't that nice?")
else:
    print("You're old!")

# Problem 3
# Ask the user to enter a number.
# Print "Fizz" if it is divisible by 3, "Buzz" if divisible by 5,
# print "FizzBuzz" if divisible by both 3 and 5,
# otherwise print the number itself.

number = int(input("Pick a number, any number!"))


# Problem 4
# Use the random module to generate a random number between 1 and 6 (inclusive).
# If the number is greater than 4, print "High roll!",
# otherwise print "Low roll!".



# Problem 5
# Ask the user for their test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
# Use nested if or elif statements.