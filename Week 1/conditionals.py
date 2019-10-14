"""
CONDITIONALS

IF STATEMENTS
Conditional statements in programming are ways for us to check for the state of
some conditions in our program and use the result to determine our next move.
The most common conditional statement is an if loop. This statement basically
checks to see "if" a certain case is true. If it is, then it executes something. If
it is not, it skips over it and does not execute it. Below is an example of a conditional
statement being used with the equal to operator to do something if a value equals 5.
"""

a = 5
if a == 5:
    print("a is 5")

b = True
if b:
    print("b was true")

"""
IF ELSE STATEMENTS
If statements alone often aren't enough for us to be able to do many meaningful things.
In order to make our conditionals more valuable, we can add something to do if the statement
we check for isn't true. This is our else block, and there's an example of how this works below.
"""

c = 6
if c == 7:
    print("c is 7")
else:
    print("c is not 7")

d = False
if d:
    print("d was true")
else:
    print("d was not true")

"""
IF ELSE IF ELSE STATEMENTS
What if we wanted to check for multiple conditions? If we want to check if multiple cases are
true, and only execute one of our statements, we can split up our conditional but using an else if 
statement. In Python, elif is used instead of else if because its commonly used and it helps make code more
readable. An example of splitting up a program like this is below.
"""

e = 9
if e == 10:
    print("e is 10")
elif e == 9:
    print("e is 9")
else:
    print("e is not 7")

f = "Hello"
if f == "Goodbye":
    print("f is Goodbye")
elif f == "Hello":
    print("f is Hello")
else:
    print("f was not hello or goodbye")