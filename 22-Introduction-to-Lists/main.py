# marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# # print(marks)
# # print(type(marks))
# # print(marks[0])
# # print(marks[1])
# # print(marks[2])
# # print(marks[3])
# # print(marks[4])
# # print(marks[5])

# # print(marks[-3]) # Negative index
# # print(marks[len(marks)-3]) # Positive index
# # print(marks[5-3]) # Positive index
# # print(marks[2]) # Positive index

# # if "6" in marks:
# #   print("Yes")
# # else:
# #   print("No")

# # Same thing applies for strings as well!
# # if "Ha" in "Harry":
# #   print("Yes")

# # print(marks[0:7])
# # print(marks[1:9])
# # print(marks[1:9:3])

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
            #0      1       2       3       4       5       6       7       8
print(animals[1:7:2])	#using positive indexes
print(len(animals))
print(animals[-7:-2])	#using negative indexes'
print(animals[2:7])

print(animals[:5])
print(animals[5:])
print(animals[5:len(animals)])
print(animals[::3])
print(animals[-8:-1:2]) # animals[1:8:2]


l1 = ["Madhu", ["Hello", 6, 9, "Megha", "hey"], 4, 10, "Vinay"]
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])

print(l1[1][0])
print(l1[1][1])
print(l1[1][2])
print(l1[1][2:])

# Assignment : Create a list which has varied elements in it like 
# list, tuple and dictionary and try accessing the elemnts within them.


# Traditional Way
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = []

for item in names:
    if "o" in item:
        namesWith_O.append(item)

print(namesWith_O)

# List Comprehension

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Length greater than 4

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
names4 = [item for item in names if len(item)>4]
print(names4)

# Assignment: You are given a list of numbers.
# Write a program that creates a new list containing 
# the square of only the even numbers from the original list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output 
# sq_even_numbers = [4, 16, 36, 64, 100]
