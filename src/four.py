import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 1000

def part_one(array):
    return
         

def part_two(array):
    return



test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array)) 

print("###########################")

input = utils.get_instructions("four", EXPECTED_LINES)
print(part_one(input)) 

print("###########################")

print(part_two(test_input_array))

print("###########################")

print(part_two(input)) 

