
name = "Madhu"
friend = "Rohan"
anotherFriend = 'Lovish'
apple = '''He said, 
Hi Madhu
hey I am good
"I want to eat an apple'''
 
print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)

str1 = """Hi, my name is
        Madhu
I am        working in
TA"""
print(str1)
print("Second last element is: ", str1[-2])


name = "Madhumitha"
    #   0123456789
    #          -2-1
print(name)
print(name[0])
print(name[9])
print(name[-2])

for character in name:
    print(character)