print(5 > 3) #Greater than, true
print(5 < 3) #Less than, false
print(5 >= 3) #Greater than or equal to, true
print(5 <= 3) #Less than or equal to, false
#When using greater/less than or equal to, the crocodile symbol goes before the equals sign.
print(5 == 5) #Equal to, true
#when doing equal to, make sure to use 2 equal signs
print(5 != 3) #Not equal to
#when using not equal to, put the exclamation mark before the equals sign.
#Use 2 equals signs for comparison, 1 equal sign for assignment to variable

a = 10
b = 7
print(a > b) #true, testing whether 10 > 7
print(a == b)#false, testing whether 10 = 7

x = int(input("Give me a number."))
y = int(input("Give me another number."))
print(x < y)

#variables can contain strings
c = "apple"
d = "banana"
print("apple" == "apple")#true, comparing whether apple = apple
print("Apple" == "apple")#false, case matters when comparing strings, comparing whether apple = Apple
#variables can be compared
print(c != d)#true, comparing whether c does not equal d
#strings can be compared by first letter, whether it is closer to a or z, a=smaller, z=bigger
print("cat" > "dog")#alphabetical comparison when using greater/less than comparators,false, comparing whether c is greater than d
print("dog" < "zebra")#true, comparing whether d is smaller than z
