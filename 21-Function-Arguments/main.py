# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")


def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy") # Hello, Amy Jhon Whatson
name("Madhu", "mitha", "R") # Hello, Madhu mitha R
name("Madhu", "mitha") # Hello, Madhu mitha Whatson

def name2(fname, lname, mname = "Jhon"):
    print("Hello,", fname, mname, lname)

name2( "Madhu", "mitha")

def name3(*name):
    print("Hello,", name[0], name[1], name[2], name[3])

name3("James", "Buchanan", "Barnes", "Phills")


def name4(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name4(mname = "Buchanan", lname = "Barnes", fname = "James")


def ctof(c):
    f = (c * 9)/5 + 32
    return f

result = ctof(39)
print(result)



def add(a,b):
    return a+b

sum = add(4,5)
mean = sum/2
print(mean)








