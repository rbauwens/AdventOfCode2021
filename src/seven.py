import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils
import itertools


EXPECTED_LINES = 1

def sum_factorial(num1, num2):
    value = abs(num2 - num1)
    sum = 0
    add =  1
    while value > 0:
        sum = sum + add
        add = add + 1
        value = value - 1
    return sum
           
    
def part_one(array, part_one = True):
    for i in range(len(array)):
        array[i] = int(array[i])

    fuel_dictionary = dict()
    for i in range(max(array)):
        fuel_dictionary[i] = 0
        for j in range(len(array)):
            if part_one:
                fuel_dictionary[i] = fuel_dictionary[i] + abs(array[j] - i)
            else:
                fuel_dictionary[i] = fuel_dictionary[i] + sum_factorial(array[j], i)
        
    least_fuel = fuel_dictionary[0]
    for key in fuel_dictionary.keys():
        if fuel_dictionary[key] < least_fuel:
            least_fuel = fuel_dictionary[key]
    return least_fuel




test_input = """16,1,2,0,4,2,7,1,2,14"""
# test_input_array = test_input.split("\n")
test_input_array = test_input.split(",")


print(part_one(test_input_array)) #37


print("###########################")

input = utils.get_instructions_single_line("seven", EXPECTED_LINES)
print(part_one(input)) #353800


print("###########################")

print(part_one(test_input_array, part_one=False))


print("###########################")

print(part_one(input, part_one=False)) #98119739



