fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz:
# nm = "Mississippi"
# print(nm[-4:-2])


# String Slicing
# M a d h u m i t h a
# 0 1 2 3 4 5 6 7 8 9

# M e g h a
# 0 1 2 3 4


name = "Madhumitha"

# print(name[0]) #M
# print(name[4]) #u
# print(len(name)) #10
# print(name[1:4])
# print(name[5:9])
# print(name[0:5])
# print(name[:5])
# print(name[5:10])
# print(name[5:])
# print(name[5:11000])

print(name[0:-3]) # print(name[0:7])
print(name[-5:-1]) # print(name[5:9])  #mith
print(name[-10:]) # print(name[0:10])
print(name[-9:]) #print(name[1:10])

# Python understands negative slicing as len(name)-3 =10-3 = 7 or skip the last 3 characters

# Outputs:
# M
# u
# 10
# adh
# mith
# Madhu
# Madhu
# mitha
# mitha
# mitha
