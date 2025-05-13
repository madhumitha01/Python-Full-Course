import pandas  # This is an example of external module
import hashlib  # This is an example of built in module
import numpy  # This is an example of external module

print("Hi")

# Dont worry about how to use these modules just yet!
df = pandas.read_csv(r"d:\PERSONAL\Python\Python-Full-Course\03-Day3-Modules-and-Pip\one.csv")
print(df)
print(df.head(n=1))

x = numpy.multiply(2,4)
print(x)

# print(pandas.read_csv(r"d:\PERSONAL\Python\Python-Full-Course\03-Day3-Modules-and-Pip\one.csv"))

m = hashlib.sha256()
print(m)

