"""
LOOPS

FOR LOOPS
A for loop basically does something either a set amount of times or goes over everything in
a collection of items once and does something with it. They can be extremely helpful in
programming because they let us do one thing to everything in a collection. Below is an
example of a for loop printing the word "Hello" five times.
"""

for x in range(5):
    print("Hello")

"""
The range that we just used above basically tells us how many iterations of the for loop were
going to do. If I'd type range 6, it would've done 6 iterations. We don't have to worry 
about how this works, just know that range is built into Python and allows us to do this in loops.
Another thing thats built into Python is len. len basically tells us how long something is, so 
if I had an array ["hello", "there", "goodbye"] calling len on the array would give me back 3 because 
thats how long the collection is. Below is an example of running a for loop over a collection.
"""

a = ["Hello", "Goodbye", "Hi"]
for x in range(len(a)):
    print(a[x])

"""
WHILE LOOPS
A while loop does something while a condition is true. You can think of this similarly to how a condition
works, but the loop will just continue to run until the condition is false. This is easier seen than
explained, so if you look at the while loop below it will help demonstrate this idea. With every iteration
of the loop, a becomes one smaller and eventually a will reach 0 and the while loop will stop executing.
"""

a = 10
while(a != 0):
    print(a)
    a -= 1