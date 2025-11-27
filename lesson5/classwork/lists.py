colors = ["red", "yellow", "green", "blue", "orange", "purple"]
           #0      1          2        3        4        5

print(colors) # Print the entire list

print("First color:", colors[0]) # Access items in a list
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])
print("Fifth color:", colors[4])
print("Sixth color:", colors[5])

# Error: list index out of range
# print(colors[10])

colors.append("pink")  # Adds an item to the end of the list
# equivalent to this:
# colors = ["red", "yellow", "green", "blue", "orange", "purple", "pink"]
print("After append:", colors)

colors.insert(2, "gray")  # Inserting an item at a specific index
# equivalent to this:
# colors = ["red", "yellow", "gray", "green", "blue", "orange", "purple", "pink"]
print("After insert at index 2:", colors)

colors.insert(0, "black")
# equivalent to this:
# colors = ["black", "red", "yellow", "gray", "green", "blue", "orange", "purple", "pink"]
print("After insert at index 0:", colors)

colors.remove("red")  # Removed the first occurence of our item
# equivalent to this:
# colors = ["black", "yellow", "gray", "green", "blue", "orange", "purple", "pink"]
print("After removing 'red':", colors)

# Error: removing item not in list.
# colors.remove("dog")

popped_color = colors.pop() # Removes and returns the last item in a list.
print("Popped color:", popped_color) 
print("After pop:", colors)
# equivalent to this:
# colors = ["black", "yellow", "gray", "green", "blue", "orange", "purple"]

popped_color_at_index = colors.pop(2) # Remove and return the item at index 2
print("Popped color at index 2:", popped_color_at_index)
print("List after color removed at index 2:", colors)
# equivalent to this:
# colors = ["black", "yellow", "green", "blue", "orange", "purple", "pink"]

colors.append("blue")
# equivalent to this:
# colors = ["black", "yellow", "green", "blue", "orange", "purple", "pink", "blue"]
blue_count = colors.count("blue") # Count how many times an item appears.
print("Count of 'blue':", blue_count)

index_of_yellow = colors.index("yellow") # Find the index of an item.
print("Index of 'yellow':", index_of_yellow)

# Error: finding the index of an item not in list
# colors.index("gray")

colors.sort() # Sorts the list: for string, alphabetical order. For integers or floats, sort smallest to largest number.
print("After sort:", colors)
# equivalent to this:
# colors = ['black', 'blue', 'blue', 'green', 'orange', 'purple', 'yellow']

colors.sort(reverse=True) # Sorts the list in reverse: for string, reverse alphabetical order. For integers or floats, sort largest to smallest number.
print("After reverse sort:", colors)
# equivalent to this:
# colors = ['yellow', 'purple', 'orange', 'green', 'blue', 'blue', 'black']

colors.reverse()  # Reverse the order of the list.
# equivalent to this:
# colors = ['black', 'blue', 'blue', 'green', 'orange', 'purple', 'yellow']
print("After reverse:", colors)