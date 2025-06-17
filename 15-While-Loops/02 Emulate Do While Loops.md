# Do-While loop in python
do..while is a special kind of loop found in other programming languages like C, Java, or JavaScript, in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

It runs a block of code:

- At least once, no matter what.
- Then checks a condition.
- If the condition is true, it repeats.
- If the condition is false, it stops.

Syntax in other languages (example in C):

```
do {
    // run this code
} while (condition);
```

## Key Feature of do...while:
The loop body runs before the condition is checked, which means it will always run at least once, even if the condition is false at the beginning.

## Why do we need do...while?
Imagine this:

You ask a user to enter a number. You want to:

Process the number once (even if it's invalid),

Then ask again only if the number doesn't meet your condition (e.g., not positive).

In this case, a regular while loop won't work well because it checks the condition first. If the condition is false from the beginning, the code inside never runs.

This is where do...while shines.

# How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:
## Example
```python 
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
```
## Output
```
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1
```
## Explanation
This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.

Here’s what’s happening:

- We create an infinite loop with while True.
- Inside, we take input and check if the condition (number > 0) fails.
- If it does, we break out of the loop.

So the code runs at least once—just like a do...while.

