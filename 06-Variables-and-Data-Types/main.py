x = 1.5
print(type(x))
y = "1"
print(type(y))
z = complex(8, 2) # => 8+2i
print(type(z))

print("The sum is:")
print(complex(8, 2) + complex(10, 5)) # 8+2i + 10+5i = 18+7i

a = complex(8, 2)
b = True
c = "Harry"
d = None
print(a)
print(b)
a1 = 9
print(a + a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))

print("List Functionality")
l1 = [1, 5, 4, "Megha", ["qwerty", "apple"], 7, (3, 4)]
print(type(l1))
print(l1)
l1.append(10) # as lists are mutable, we can add/modify an element once it's created
print(l1)

print("Tuple Functionalities")
t1 = (1, 7, 9, (3, "abc"), [78, "house"])
print(t1)
print(type(t1))
# t1.append(10) # Throws an error as tuples are immutable

dict2 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict2.pop("age"))


list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)