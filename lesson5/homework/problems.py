import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
print("Psst! Remember the savings code from your last testing factory visit! It will help you!")
print("Welcome back to the testing factory!")
print("Testing already available material...")
os_list = ["Windows", "macOS", "Linux"]
print("Testing results:", os_list[len(os_list) - 1])
os_list.reverse()
print("Testing results:", os_list)



# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
schoolSubjects = ["ELA", "Mathematics", "Social Studies", "Science"]
print("Testing already available material...")
print("Testing results:", schoolSubjects[1])
schoolSubjects.sort()
print("Testing results:", schoolSubjects)



# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
errors = ["400", "401", "403", "404", "500"]
print("Testing already available data...")
print("Testing results:", len(errors))
print("Testing results:", errors.index("403"))



# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random
langs = ["Python", "Java"]
print("Testing already available material...")
print("Testing results:", random.choice(langs))
langs.append("C++")
print("Testing results:", langs)



# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot"]
print("Testing already available material...")
middle = passwords[len(passwords) // 2]
print("Testing results:", middle)
passwords.pop(0)
print("Testing results:", passwords)

paytimeCode = input("Paytime! Please enter savings code:")
if paytimeCode == "KDHEU937432":
    print("Please pay $80.")
else:
    print("Please pay $100.")
print("Payment is given via child wearing handsome blazer.")
print("Thank you!")
