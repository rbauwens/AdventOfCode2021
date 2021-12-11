import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 10

def process_array(array):
    num_dict = dict()
    #rows
    down = len(array)
    #columns
    across = len(array[0])
    
    for i in range(down):
        for j in range(across):
            num_dict[(i, j)] = [int(array[i][j]), False, False]
            
    return num_dict, down, across

def execute_flash(num_dict, key, down, across):
    i = key[0]
    j = key[1]
    #upperleft
    if (i>0) and (j>0):
        num_dict[(i-1, j-1)][0] = num_dict[(i-1, j-1)][0] + 1
    #above
    if (i>0):
        num_dict[(i-1, j)][0] = num_dict[(i-1, j)][0] + 1
    # upper right
    if (i>0) and (j<across - 1):
        num_dict[(i-1, j+1)][0] = num_dict[(i-1, j+1)][0] + 1
    # left
    if (j > 0):
        num_dict[(i, j-1)][0] = num_dict[(i, j-1)][0] + 1
    #right
    if (j < across - 1):
        num_dict[(i, j+1)][0] = num_dict[(i, j+1)][0] + 1
    
    # lower left
    if (i <  down - 1) and (j>0):
        num_dict[(i+1, j-1)][0] = num_dict[(i+1, j-1)][0] + 1
    # below
    if (i < down - 1):
        num_dict[(i+1, j)][0] = num_dict[(i+1, j)][0] + 1
    # lower right
    if (i <  down - 1) and (j < across -1):
        num_dict[(i+1, j+1)][0] = num_dict[(i+1, j+1)][0] + 1
    
    return num_dict

def process_step(num_dict, down, across):
    flashes = 0
    for key in num_dict.keys():
        num_dict[key][0] = num_dict[key][0] + 1
    change = True
    while change:
        change = False
        for key in num_dict.keys():
            if num_dict[key][0] > 9:
                if num_dict[key][2] == True:
                    continue
                else:
                    change = True
                    num_dict[key][1] = True
                    
                    flashes = flashes + 1
                    num_dict = execute_flash(num_dict, key, down, across)
                    num_dict[key][2] = True
                    # num_dict[key][0] = 0
    for key in num_dict.keys():
        if num_dict[key][2] == True:
            num_dict[key][2] = False
            num_dict[key][1] = False
            num_dict[key][0] = 0
    return flashes

def part_one(array):
    num_dict, down, across = process_array(array)
    total_flashes = 0
    for i in range(100):
        num_flashes = process_step(num_dict, down, across)
        total_flashes = total_flashes + num_flashes
        # print("after step {}: num_flashes: {}".format(i + 1, num_flashes))
    
    return total_flashes

def part_two(array):
    num_dict, down, across = process_array(array)
    octopuses = down*across
    print("oct: ", octopuses)
    i = 0
    while True:
        i = i + 1
        num_flashes = process_step(num_dict, down, across)
        if num_flashes == octopuses:
            return i


test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array)) 

print("###########################")

input = utils.get_instructions("eleven", EXPECTED_LINES)
print(part_one(input)) 

print("###########################")

print(part_two(test_input_array))

print("###########################")

print(part_two(input)) 

