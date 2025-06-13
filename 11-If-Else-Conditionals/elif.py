num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999 or num == 745):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

age = int(input("Enter your age: "))
# Conditional operators 
# >, <, >=, <=, ==, !=

if(age>18):
    print("You can drive!")
    print("You are good to go!!")
elif(age==18):
    print("We will have to evaluate you!!")
else:
    print("You can't drive!")
    print("Wait until you become 18 yrs")

print("This is end of program!")
