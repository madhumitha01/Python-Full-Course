# Python while Loop
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop. 
## Example:

```python 
count = 5
while (count > 0):
  print(count)
  count = count - 1 # count-- (or) count-=1
```
## Output:
```
5
4
3
2
1
```

Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

# Why use while loop instead of for loop?
➤ Use a for loop when:
You know exactly how many times you want to run the loop (like for each item in a list or for a range of numbers).
```
for i in range(5):
    print(i)
```
This will run exactly 5 times. It's perfect when the number of repetitions is pre-decided.

➤ Use a while loop when:
You don’t know in advance how many times you need to loop.
Maybe you're waiting for user input, a condition to change, or data to become available.

```
password = ""
while password != "secret345":
    password = input("Enter password: ")
```
You don't know how many tries a user will take to type the correct password, so while makes more sense here.



# Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed. 

When the loop ends normally (not because of a break), the else block runs.

This is not very common in most coding scenarios, but it’s useful when you want to do something after the loop finishes without being interrupted.

## Example:

```python 
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
```
## Output:
```
5
4
3
2
1
counter is 0
```
