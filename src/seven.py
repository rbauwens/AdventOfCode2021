import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 1


def part_one(array, days):
    for i in range(len(array)):
        array[i] = int(array[i])

    for day in range(0,days):
        # print("day ", day)
        new_fish = 0
        for i in range(len(array)):
            if array[i] == 0:
                new_fish = new_fish + 1
                array[i] = 6
            else:
                array[i] = array[i] - 1
        for j in range(0, new_fish):
            array.append(8)
        # print(array)
    return len(array)


def part_two(array, days):
    for i in range(len(array)):
        array[i] = int(array[i])
    fish_dictionary = dict()
    for i in range(0,9):
        fish_dictionary[i] = array.count(i)
    
    for day in range(0, days):
        new_dictionary = dict()
        for i in range(0,8):
            new_dictionary[i] = fish_dictionary[i+1]
        new_dictionary[6] = new_dictionary[6] + fish_dictionary[0]
        new_dictionary[8] = fish_dictionary[0]
        fish_dictionary = new_dictionary.copy()

    sum = 0
    for key in fish_dictionary.keys():
        sum = sum + fish_dictionary[key]
    return sum
    



test_input = """3,4,3,1,2"""
# test_input_array = test_input.split("\n")
test_input_array = test_input.split(",")

print("18 Days")
print(part_one(test_input_array.copy(), 18)) 
print("80 Days")
print(part_one(test_input_array.copy(), 80)) 

print("###########################")

input = utils.get_instructions_single_line("six", EXPECTED_LINES)
print(part_one(input.copy(), 80)) 

print("###########################")

print(part_two(test_input_array.copy(), 18))
print(part_two(test_input_array.copy(), 80))
print(part_two(test_input_array.copy(), 256))

print("###########################")

print(part_two(input.copy(), 256)) 



