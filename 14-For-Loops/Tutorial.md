# Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types; 
- for loop
- while loop 
# The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

## Simple Analogy to Understand
“Imagine you're a postman. You have 5 houses to deliver letters to. You walk down the street and deliver one letter at a time.”

Let's say:
```python
houses = ["House 1", "House 2", "House 3", "House 4", "House 5"]
```

Now, we do:
```python
for house in houses:
    print("Delivering letter to", house)
```
### What this code does?
- Python is like the postman.
- The list is the row of houses.
- The house variable is like the current house where the postman is standing.
- The loop says: “For each house, deliver the letter.”

Output:
```
Delivering letter to House 1
Delivering letter to House 2
```

### *“Python doesn’t do everything at once. It takes one item, does something, then goes to the next. That’s called iteration.”*

## Example: iterating over a string:

```python 
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```
## Output:

A, b, h, i, s, h, e, k,
 

## Example: iterating over a list:

``` python 
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```
## Output:

Red\
Green\
Blue\
Yellow

Similarly, we can use loops for lists, sets and dictionaries.
## range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

## Example:
```python
for k in range(5):
    print(k)
```
## Output:

0\
1\
2\
3\
4\
Here, we can see that the loop starts from 0 by default and increments at each iteration.

 

But we can also loop over a specific range.

## Example:
```python
for k in range(4,9):
    print(k)
```
## Output:

4\
5\
6\
7\
8

## Quick Quiz
Explore about third parameter of range (ie range(x, y, z))
