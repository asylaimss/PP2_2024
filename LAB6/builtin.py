#1
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Multiplication result:", result)

#2
def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = "Hello World"
upper, lower = count_case(input_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

#3
def is_palindrome(string):
    clean_string = string.lower().replace(" ", "")
    return clean_string == clean_string[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4
import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    square_root = math.sqrt(number)
    return square_root

number = 25100
milliseconds = 2123
result = calculate_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#5
def all_true_elements(tuple_data):
    return all(tuple_data)


tuple_data = (True, True, True, True)
print(all_true_elements(tuple_data))  # True

tuple_data = (True, False, True, True)
print(all_true_elements(tuple_data))  # False
