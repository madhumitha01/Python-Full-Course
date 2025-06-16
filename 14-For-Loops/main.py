name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")


# i='A' => A
# i='b' => b This is something special!
# i='h' =>h

    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)


# color = Red => Red 
#         i = R e d
# color = Green =>Green
#         i=G r e e n

for k in range(5):
  print(k + 1)

# k = 0 => 1
# k =1  =>2
# k=4 =>5
  
# for k in range(1, 20001):
#   print(k)

  
for k in range(1, 12, 3):
  print(k)

for k in range(1, 12, 2):
  print(k)

1
3
5
7
9
11


# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# range(1,n-1)
for i in range(4):
    print(i)