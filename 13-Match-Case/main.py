
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

# Using if-Else Condition
x = int(input("Enter the value of x: "))
if (x==0):
    print("x is zero")
elif (x==4):
    print("case is 4")
elif (x>10):
    print("x >10")
else:
    print(x)

# Using Match Case
x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x > 10:
        print("x is > 10")
    case _:
        print(x)