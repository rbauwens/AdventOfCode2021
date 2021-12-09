import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 100


def process_input(array):
    all_lines = []
    for i in range(len(array)):
        line_array = []
        for j in range(len(array[i])):
            line_array.append(int(array[i][j]))
        all_lines.append(line_array)
    return all_lines
        
def is_lower(array, i, j, MAX_I, MAX_J):
    my_num = array[i][j]
    lower = True
    if j != 0:
        left = array[i][j-1]
        if my_num >= left:
            return False
    if i != MAX_I:
        down = array[i+1][j]
        if my_num >= down:
            return False
    if j != MAX_J:
        right = array[i][j+1]
        if my_num >= right:
            return False
    if i != 0:
        up = array[i-1][j]
        if my_num >= up:
            return False
    return True


def part_one(array, part_two = False):
    map = process_input(array)
    MAX_I = len(map)
    MAX_J = len(map[0])
    lower_count = 0
    basin_dict = dict()
    for i in range(MAX_I):
        for j in range(MAX_J):
            lower = is_lower(map, i, j, MAX_I-1, MAX_J-1)
            if lower:
                basin_dict[(i,j)] = []
                lower_count = lower_count + map[i][j] + 1
    if part_two:
        return lower_count, basin_dict, map, MAX_I, MAX_J
    return lower_count

def get_basin_size(map, basin, max_i, max_j):
    for key in basin:
        i = key[0]
        j = key[1]

        # right
        if j != max_j:
            j = j + 1
            entry = map[i][j]
            while (entry != 9) and (j <= max_j):
                entry = map[i][j]
                if entry != 9:
                    if (i,j) not in basin:
                        basin.append((i,j))
                j = j + 1
                
        # left
        i = key[0]
        j = key[1]
        if j != 0:
            j = j - 1
            entry = map[i][j]
            while entry != 9 and j >=0:
                entry = map[i][j]
                if entry != 9:
                    if (i,j) not in basin:
                        basin.append((i,j))
                j = j - 1
        
        # down
        i = key[0]
        j = key[1]
        if i != max_i:
            i = i + 1
            entry = map[i][j]
            while entry != 9 and i <= max_i:
                entry = map[i][j]
                if entry != 9:
                    if (i,j) not in basin:
                        basin.append((i,j))
                i = i + 1
                
        # up
        i = key[0]
        j = key[1]
        if i != 0:
            i = i - 1
            entry = map[i][j]
            while entry != 9 and i >=0:
                entry = map[i][j]
                if entry != 9:
                    if (i,j) not in basin:
                        basin.append((i,j))
                i = i - 1
            
    
    return len(basin)
    
def get_product(basins):
    basins.sort()    
    return ((basins[-3]) * (basins[-2]) * (basins[-1]))

def part_two(array):
    _, basin_dict, map, max_i, max_j= part_one(array, part_two=True)
    basins = []
    for key in basin_dict.keys():
        # print(key)
        basin = []
        basin.append((key[0], key[1]))
        size = get_basin_size(map, basin, max_i-1, max_j-1)
        # print(size)
        basins.append(size)
    return get_product(basins)

            




test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array)) 

print("###########################")

input = utils.get_instructions("nine", EXPECTED_LINES)
print(part_one(input)) 

print("###########################")

print(part_two(test_input_array))

print("###########################")

print(part_two(input)) 

