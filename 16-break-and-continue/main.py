for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)

# i = 0 -> 5 X 0 = 0
# i = 1 -> 5 X 1 = 5
# i = 2 -> 5 X 2 = 10
# .
# .
# .
# i =10 ->  Skip the iteration
# i =11 -> s X 11 = 55
  
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break



# BREAK
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")


# CONTINUE
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

# i = 2  2%2 = 0 is 0!=0? False skips IF 2
# i = 3  3%2 = 1 is 1!=0? True enters IF