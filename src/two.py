import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 1000


def part_one(array):
    horiz_pos = 0
    depth = 0
    for i in range(len(array)):  
        keyword = array[i].split(" ")[0]
        distance = int(array[i].split(" ")[1])
        if keyword == "forward":
            horiz_pos = horiz_pos + distance
        elif keyword == "up":
            depth = depth - distance
        elif keyword == "down":
            depth = depth + distance
      
    print("horiz: {}".format(horiz_pos))
    print("depth: {}".format(depth))
    return horiz_pos*depth
  
        

def part_two(array):
    horiz_pos = 0
    depth = 0
    aim = 0
    for i in range(len(array)):  
        keyword = array[i].split(" ")[0]
        distance = int(array[i].split(" ")[1])
        if keyword == "forward":
            horiz_pos = horiz_pos + distance
            depth = depth + (aim * distance)
        elif keyword == "up":
            aim = aim - distance
        elif keyword == "down":
            aim = aim + distance
      
    print("horiz: {}".format(horiz_pos))
    print("depth: {}".format(depth))
    return horiz_pos*depth



test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("two", EXPECTED_LINES)

print(part_one(input))
print("###########################")
print(part_two(test_input_array))
print(part_two(input))

