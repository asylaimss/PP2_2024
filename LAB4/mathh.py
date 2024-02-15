#1 Write a Python program to convert degree to radian.
"""
import math
x = int(input())
print(math.radians(x)) 

"""
from math import radians
print(radians(int(input())))

#2 Write a Python program to calculate the area of a trapezoid.
a = float(input())
b = float(input())
c = float(input())
print(((b + c)*0.5)*a)

#3 Write a Python program to calculate the area of regular polygon.
from math import tan, pi
n = int(input())
a = int(input())
area = n * (a ** 2) / (4 *tan(pi/n))
print(area)

#4 Write a Python program to calculate the area of a parallelogram.
print(float(input()) * float(input()))