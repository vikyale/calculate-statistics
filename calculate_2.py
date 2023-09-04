# 1 : User Input via input() function:  Get a list of numbers as input from the user
#########################################

input_numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = [int(x) for x in input_numbers.split()]

from statistics import mean, median, mode

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

# 2 : Predefined List:
#########################################
numbers = [12, 34, 56, 23, 67, 12, 45, 78, 23, 12]

from statistics import mean, median, mode

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

#3 File Input,  Assuming numbers.txt contains one number per line
 
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

from statistics import mean, median, mode

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")


