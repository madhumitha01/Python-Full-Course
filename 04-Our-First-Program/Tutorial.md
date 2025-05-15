# Day 4 - Our First Program

Today we will write our first ever python program from scratch. It will consist of a bunch of print statements.
print can be used to print something on the console in python

# More on Print statement
The syntax of a print statement looks something like this:

```python
print(object(s), sep=separator, end=end, file=file)
```

## Other Parameters of Print Statement 
1. object(s): Any object, and as many as you like. Will be converted to string before printed
2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
3. end='end': Specify what to print at the end. Default is '\n' (line feed)
4. file: An object with a write method. Default is sys.stdout

Parameters 2 to 4 are optional

## Example Code

```python
# Basic print
print("Hello", "world")  
# Output: Hello world
# Default separator is a space, and it ends with a newline

# Using a custom separator
print("Hello", "world", sep="-")  
# Output: Hello-world

# Using a custom end
print("Hello", end=" ")
print("world")  
# Output: Hello world
# The first print ends with a space instead of a newline

# Combining both sep and end
print("Python", "is", "fun", sep="*", end="!!!\n")
# Output: Python*is*fun!!!

# Redirecting output to a file
with open("output.txt", "w") as f:
    print("This will go into a file", file=f)
```

## Quick Quiz

Write a program to print a poem in Python. Choose the poem of your choice and publish your repl


```python
print("---Your poem here---")

```

Please make sure you attempt this. Might be easy for some of you but please finish each and every task