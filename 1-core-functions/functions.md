For each of the following functions, find the official python3
documentation for the function, write a 1 sentence comment describing each function and 1-4 lines of code demonstrating a use case.

[random.randint(0,99) for _ in 20] is a useful way to produce a sample list for these. if you need dummy strings, chr(randint(ord('A'), ord('B'))) produces random letters of the alphabet.

It's ok if this exercise takes a few days. Do a little each day through the rest of the week.

```
print() # and the file, end, and sep parameters
input()
# the .is methods of strings (isalpha() isalnum() etc)
math.isclose() # look at (.1 + .2) == .3
round()
len()
sum()
# type functions (int(), float(), str(), dict(), tuple(), list(), set())
list()
map()
filter()
functools.reduce()
all()
any()
zip()
enumerate()
range()
count()
max()
min()
pow()
repr() # what is the difference between repr and str?
sorted() # vs .sort() & the key parameter of these functions.
reversed()
type()
isinstance()

# string methods
.format()
# .is functions (.isalpha(), .isalnum(), etc)
# transformation functions .upper(), .lower() etc
.encode()
.strip(), .lstrip(), .rstrip()
.split(), .splitlines()
.join() # this one is weird but can be very useful

# what do the \u and \N (note the capital) escapes do?

# if your terminal is using a really complete font, you can print out emojis. give it a try.

# what is a bytes object? how does it relate to strings and character sets?

# list methods:
.append()
.extend()
.insert()
.remove()
.pop()
.clear()
.index()
.count()
.sort()
.copy()

# dictionary methods:
.get()
.keys()
.values()
.items()
.update()
.clear()
.pop()
.popitem()
# what does sorted() do when given a dictionary?
# can you figure out how to sort a dictionary by its values?
