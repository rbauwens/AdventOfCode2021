import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 828


def part_one(array):
    return 



test_input_one = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
test_input_array = test_input_one.split("\n")

print(part_one(test_input_array)) 

print("###########################")

# input = utils.get_instructions("fourteen", EXPECTED_LINES)
# print(part_one(input))  

# print("###########################")
# print(part_two(test_input_array)) 


# print("###########################")
# print(part_two(input)) 


