
# Day 6 - Variables and Data Types
## What is a variable?
Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc
Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
```python
a = 1
b = True
c = "Harry"
d = None
```

These are four variables of different data types.

## What is a Data Type?
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error. \
In python, we can print the type of any operator using type function:
```python
a = 1
print(type(a))
b = "1"
print(type(b))
```
By default, python provides the following built-in data types:

## 1. Numeric data: int, float, complex


 - int: 3, -8, 0
 -    float: 7.349, -9.0, 0.0000001
 -  complex: 6 + 2i 

 ## 2. Text data: str
    

str: "Hello World!!!", "Python Programming"

## 3. Boolean data:
    

Boolean data consists of values True or False.

## 4. Sequenced data: list, tuple
    

**list:**  A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

🔹 What does "mutable" mean?
If an object is mutable, it means:

You can change its contents after it is created.

**Example:**

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```


Output:

```markup
[8, 2.3, [-4, 5], ['apple', 'banana']]
```


**Tuple:**  A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation. 

**Example:**

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```


Output:

```python
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
```


## 5. Mapped data: dict
    

**dict:** A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets. Dictionaries are immutable.

**Example:**

```python
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
```


Output:

```python
{'name': 'Sakshi', 'age': 20, 'canVote': True}
```

## A list can contain:
- Tuples
- Dictionaries
- Other lists
- Any data type (including custom objects)

**Example:**

```python
my_list = [
    (1, 2),                  # tuple
    {"name": "Alice"},       # dictionary
    [3, 4, 5],               # another list
    42,                      # integer
    "hello"                  # string
]
```

## A tuple can contain:
- Lists
- Dictionaries
- Other tuples
- Any data type

**Example:**

```python
my_tuple = (
    [1, 2, 3],               # list
    {"key": "value"},        # dictionary
    (4, 5),                  # another tuple
    3.14                     # float
)
```

## A dictionary can contain:
- Lists, tuples, or other dictionaries as values
- Tuples as keys (if immutable)
- Lists or dictionaries cannot be keys (they’re mutable and unhashable)

### Why?
- Dictionaries in Python use a hash table internally for fast lookup.
- Every key in a dictionary must have a fixed hash value (obtained using Python's built-in hash() function).
- If the key can change (i.e., it's mutable), its hash would also change — and the dictionary wouldn't be able to find or store it properly.

➤ Key Rule: 🔑Only immutable (and hashable) types can be used as dictionary keys.

| Type        | Can be Key? | Can be Value? |
| ----------- | ----------- | ------------- |
| `str`       | ✅           | ✅             |
| `int/float` | ✅           | ✅             |
| `tuple`     | ✅\*         | ✅             |
| `list`      | ❌           | ✅             |
| `dict`      | ❌           | ✅             |

✅* Tuples can be keys only if all their elements are also immutable (no lists or dicts inside).

**Example:**

```python
my_dict = {
    "list": [1, 2, 3],
    "tuple": (4, 5),
    "dict": {"a": 1},
    (1, 2): "tuple as key"   # valid
    # [1, 2]: "list as key"  # ❌ would raise TypeError as List used as key
}
```
