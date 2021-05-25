# Use join
# This is a powerful technique that takes advantage of Python’s iterator protocol.
# This technique reverses a string using reverse iteration with the reversed()
# built-in function to cycle through the elements in the string in reverse order and then use .join() method
# to merge all of the characters resulting from the reversed iteration into a new string.

string = 'pralay'
reversed_str = '' .join(reversed(string))
print("Reversed string is: ", reversed_str)

