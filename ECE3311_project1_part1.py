import numpy as np
import matplotlib


#Question 1
x=21
y="My kid is "
z=" months old today!"
x=str(x)
a=y + x +z #string concatenation
print(a)
#output: My kid is 21 months old today!

#Question 2
#A list is a mutable data type that can be edited while a tuple is immutable.
#Operations such as inserting or removing elements can be performed on a list.
#Lists have more built in methods than tuples.


#Question 3
for x in range(3):
    print("Stranger Things Season 3 was totally awesome!")
print("I cannot wait for Stranger Things Season 4.")

for x in range(3):
    print("Stranger Things Season 3 was totally awesome!")
for x in range(3):
    print("I cannot wait for Stranger Things Season 4.")


#Question 4
def sequence():
    numarray = [None] * 9
    for i in range(9):
        numarray[i] = -4 + i
    print(numarray)
#Output: [-4, -3, -2, -1, 0, 1, 2, 3, 4]

#Question 5
class Foo2:
    def __init__(value):
        value = 10
    def __subtract_one__(value):
        value = value - 1
    def __multiply__three(value):
        value = value * 3

    







        
