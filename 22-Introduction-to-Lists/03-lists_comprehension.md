# List Comprehension
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

 

## Syntax:

List = [Expression(item) for item in iterable if Condition]

**Expression**: It is the item which is being iterated.

**Iterable**: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

**Condition**: Condition checks if the item should be added to the new list or not. 

Basically, remember it as:
```
[what_you_want_to_add for each_item in original_list if condition]
```

### Example 1: Accepts items with the small letter “o” in the new list 

##### Traditional way:
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = []

for item in names:
    if "o" in item:
        namesWith_O.append(item)

print(namesWith_O)
```

##### Using List comprehension:
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
```
### Output:
```
['Milo', 'Bruno', 'Rosa']
 ```

### Example 2: Accepts items which have more than 4 letters
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
```
### Output:
```
['Sarah', 'Bruno', 'Anastasia']
```
