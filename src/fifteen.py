import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils
import numpy
from collections import Counter


EXPECTED_LINES = 102


def part_one(input_array, steps):
    return

    


test_input_one = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
test_input_array = test_input_one.split("\n")

print(part_one(test_input_array, 10)) 

print("###########################")

# input = utils.get_instructions("fourteen", EXPECTED_LINES)
# print(part_one(input, 10))  

# print("###########################")
# print(part_two(test_input_array)) 


# print("###########################")
# print(part_two(input)) 


