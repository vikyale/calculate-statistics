"""
Developed a Python program that efficiently calculates and displays 
the mean, median, and mode of a list of numbers, demonstrating foundational 
understanding of Python syntax and basic statistics.
"""

import math
import statistics

arr = []

val1 = arr.append(float(input("Please add new value 1: ")))
val2 = arr.append(float(input("Please add new value 2: ")))
val3 = arr.append(float(input("Please add new value 3: ")))
val4 = arr.append(float(input("Please add new value 4: ")))

mean = statistics.mean(arr)
median = statistics.median(arr)
mode = statistics.mode(arr)

print("The mean is "+str(mean))
print("The median is "+str(median))
print("The mode is "+str(mode))
