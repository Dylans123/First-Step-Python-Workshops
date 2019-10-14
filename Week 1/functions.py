"""
FUNCTIONS

In programming often times we write code that we want to reuse many times.
It can be difficult if we have to write all of our code together and have
no way of deciding which code we want to execute and when. The way this problem is
solved is by splitting our code up into functions and then calling them wherever we need to
use that little bit of code. This helps us write a lot less code and solve problems that previously
we wouldn't have been able to. Below is an example of declaring a function in Python.
"""

def printMyWords(words):
    print(words)

printMyWords("Hello there")

"""
Lets go line by line and explain what's happening above. On line 12 we write def and then
printMyWords(words). Whenever you want to create a function in Python, all you have to do
is write def followed by a space and what you want to call your function. Following def, youll have
the name of your function and what you want to pass into your function (In this case a variable called words).
On line 15, were calling our function by just writing the name of our function and then what we want to pass into
it in parentheses. Just think of this as declaring whats in the parentheses when you call the function to be
the variable thats getting passed in (So in this case we're declaring the varibale words to be equal to the
string hello there).

FUNCTIONS WITH A TWIST
Inside a function, we can do anything that we've already gone over. So that includes loops, conditionals, etc.
Below is an example of using a conditional in a function.
"""

def printTheNumber(number):
    if number == 10:
        print("The number is 10")
    elif number == 11:
        print("The number is 11")
    else:
        print("The number was neither 10 nor 11")

printTheNumber(10)