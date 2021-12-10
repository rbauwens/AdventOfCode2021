import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 106

def part_one(array):
    return

def part_two(array):
    return


test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array)) 

print("###########################")

input = utils.get_instructions("ten", EXPECTED_LINES)
print(part_one(input)) 

print("###########################")

print(part_two(test_input_array))

print("###########################")

print(part_two(input)) 

