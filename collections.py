"""
COLLECTIONS

EXPLANATION
A collection of elements also represent things we have in the real world. 
A good example of a collection in the real world is a list. Collections are just 
ways in programming for us to group things together logically, like put names together 
or test scores. Below is an example of the two most common types of collections in Python, 
arrays and dictionaries.
"""

#Array of names
names = ["Dylan", "Garrett", "Tom"]

#Dictionary of names and phone numbers
numbers = {"Dylan": 1234567890, "Tom": 0987654321}

"""
ARRAYS
Arrays are basically the exact same as a list in programming. In order to
get a value out of an array, we type the name of the array followed by braces [] with
the position of the array we want inside the braces. We start counting which
element is at which place by starting at 0, so in the names array the value at names[0]
is "Dylan". The below statements in order would print out "Dylan" then "Garrett" then "Tom".
"""

print(names[0])
print(names[1])
print(names[2])

"""
DICTIONARIES
Dictionaries in Python function the same way as a dictionary in real life. The same way you look up
a words definition by the word itself, you can look up a value in a dictionary by its key. In
the numbers dictionary, they keys are "Dylan" and "Tom". "Dylan" corresponds to the value 1234567890
and "Tom" corresponds to the value 0987654321. You index into a dictionary the same way you index into
an array, by typing the name followed by brackets and the key which you want to get. The two statements below
will give you 1234567890 then 0987654321.
"""

print(numbers["Dylan"])
print(numbers["Tom"])