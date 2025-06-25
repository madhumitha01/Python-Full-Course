def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
 

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)


def welcome(name):
    print("Welcome to the program", name)

welcome("Madhu")
welcome("Megha")
welcome("Vinay")


name = input("Enter the name:")
welcome(name)




def calculateAverage(num1, num2):
    avg = (num1+num2)/2
    print("The average is:", avg)

calculateAverage(4,5)
calculateAverage(56,100)


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
avg = (num1+num2)/2
print("The average is:", avg)