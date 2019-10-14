"""
OPERATORS

BASIC OPERATORS
In programming, most of the basic mathematical operators that your used to you can also use
the same way in programming. Below are some examples of using the +, -, *, /, and % operators.
"""

#Initialize the value of a
a = 5
print("The value of a is: ", a)

#Addition
b = a + 1
print("The value of a + 1 is: ", b)

#Subtraction
c = a - 1
print("The value of a - 1 is: ", c)

#Multiplication
d = a * 2
print("The value of a * 2 is: ", d)

#Division
e = a / 2
print("The value of a / 2 is: ", e)

#Remainder
f = a % 2
print("The remainder of dividing a by 2 is: ", f)

"""
OPERATORS MIXED WITH DECLARATIONS
In the above example, we were doing all these operations to a but declaring the result
to be different variables. If we want to actually alter the value of a as we go, we
can do that with a shorthand that Python gives us. Below is an example of this.
"""

#Initialize the value of a
a = 5
print("The value of a is: ", a)

#Addition
a += 1
print("The value of a + 1 is: ", a)

#Reset the value of a
a = 5
print("The value of a is: ", a)

#Subtraction
a -= 1
print("The value of a - 1 is: ", a)

#Reset the value of a
a = 5
print("The value of a is: ", a)

#Multiplication
a *= 2
print("The value of a * 2 is: ", a)

#Reset the value of a
a = 5
print("The value of a is: ", a)

#Division
a /= 2
print("The value of a / 2 is: ", a)

#Reset the value of a
a = 5
print("The value of a is: ", a)

#Remainder
a %= 2
print("The remainder of dividing a by 2 is: ", a)

"""
OPERATORS FOR COMPARISON
There are also operators that allow us to compare two values too each other.
These can actually go quite in depth and get rather complicated, so instead were
going to focus on the five most common ones that were going to be using for the moment being.
These operators are listed below. All of the below print statements will print out a boolean
that will be true or false depending on whether the statement inside the print statement is
true or false.
"""

#Equal too
print(5 == 5)

#Less than or equal too
print(5 <= 5)

#Greater than or equal too
print(5 >= 5)

#Less than
print(5 < 5)

#Greater than
print(5 > 5)