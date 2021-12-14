import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils
import numpy
from collections import Counter


EXPECTED_LINES = 102

def get_final(array):
    count = Counter(array)
    first = True
    for key in count.keys():
        if first:
            max = count[key]
            min = count[key]
            first = False
        else:
            if count[key] > max:
                max = count[key]
            if count[key] < min:
                min = count[key]
    print("max: ", max)
    print("min: ", min)
    return max - min

def get_final2(array):
    count = Counter(array.items())
    first = True
    for key in count.keys():
        if first:
            max = count[key]
            min = count[key]
            first = False
        else:
            if count[key] > max:
                max = count[key]
            if count[key] < min:
                min = count[key]
    print("max: ", max)
    print("min: ", min)
    return max - min


# def part_one(input_array, steps):
#     starting = input_array[0]
#     start_list = list(starting)
#     array = numpy.array(start_list)
#     rule_dict = dict()
#     for line in input_array[2:]:
#         pairswap = line.split(" -> ")[0] 
#         rule_dict[(pairswap[0], pairswap[1])] = line.split(" -> ")[1]
    
#     for step in range(steps):
#         size = 2
#         shape = array.shape[:-1] + (array.shape[-1] - size + 1, size)
#         strides = array.strides + (array. strides[-1],)
#         # print(numpy.lib.stride_tricks.as_strided(array, shape=shape, strides=strides))
#         pairs = []
#         for pair in numpy.lib.stride_tricks.as_strided(array, shape=shape, strides=strides):
#             if (pair[0], pair[1]) in rule_dict.keys():
#                 new_str = [pair[0], rule_dict[(pair[0], pair[1])], pair[1]]
#                 pairs.append(new_str)
#         new_array = pairs[0]
#         for pair in pairs[1:]:
#             new_array.append(pair[1])
#             new_array.append(pair[2])
#         # print("step ", step)
#         # print(new_array)
#         # print(len(new_array))
#         array = numpy.array(new_array)
#     return get_final(array)
     

def get_array(array, steps, rule_dict):
    for step in range(steps):
        size = 2
        shape = array.shape[:-1] + (array.shape[-1] - size + 1, size)
        strides = array.strides + (array. strides[-1],)
        # print(numpy.lib.stride_tricks.as_strided(array, shape=shape, strides=strides))
        pairs = []
        for pair in numpy.lib.stride_tricks.as_strided(array, shape=shape, strides=strides):
            if (pair[0], pair[1]) in rule_dict.keys():
                new_str = [pair[0], rule_dict[(pair[0], pair[1])], pair[1]]
                pairs.append(new_str)
        new_array = pairs[0]
        for pair in pairs[1:]:
            new_array.append(pair[1])
            new_array.append(pair[2])
        # print("step ", step)
        # print(new_array)
        # print(len(new_array))
        array = numpy.array(new_array)
    return array

def part_one(input_array, steps):
    starting = input_array[0]
    start_list = list(starting)
    array = numpy.array(start_list)
    rule_dict = dict()
    for line in input_array[2:]:
        pairswap = line.split(" -> ")[0] 
        rule_dict[(pairswap[0], pairswap[1])] = line.split(" -> ")[1]
    
    size = 2
    shape = array.shape[:-1] + (array.shape[-1] - size + 1, size)
    strides = array.strides + (array. strides[-1],)
    # print(numpy.lib.stride_tricks.as_strided(array, shape=shape, strides=strides))
    arrays = []
    for pair in numpy.lib.stride_tricks.as_strided(array, shape=shape, strides=strides):
        array = get_array(pair, steps, rule_dict)
        arrays.append(array)
    new_array = arrays[0].tolist()
    
    for litte_array in arrays[1:]:
        new_array.extend(litte_array[1:].tolist())
    
    return get_final(new_array)

def part_two(input_array):

    starting = input_array[0]
    start_list = list(starting)
    array = numpy.array(start_list)
    rule_dict = dict()
    for line in input_array[2:]:
        pairswap = line.split(" -> ")[0] 
        rule_dict[(pairswap[0], pairswap[1])] = line.split(" -> ")[1]

    element_dict = dict()
    for char in starting:
        if char in element_dict.keys():
            element_dict[char] = element_dict[char] + 1
        else:
            element_dict[char] = 1

    pairs_dict = dict()
    for i in range(len(start_list)-1):
        pair_array = start_list[i:i+2]
        pair = (pair_array[0], pair_array[1])
        if pair in pairs_dict.keys():
            pairs_dict[pair] = pairs_dict[pair] + 1
        else:
            pairs_dict[pair] = 1
    
    for step in range(40):
        # print("step ", step)
        # print(element_dict)
        # print(sum(element_dict.values()))
        new_pairs_dict = pairs_dict.copy()
        for pair in pairs_dict.keys():
            if pair in rule_dict.keys():
                amount = pairs_dict[pair]
                new_pair1 = (pair[0], rule_dict[pair])
                new_pair2 = (rule_dict[pair], pair[1])
                
                if new_pair1 in new_pairs_dict.keys():
                    new_pairs_dict[new_pair1] = new_pairs_dict[new_pair1] + amount
                else:
                    new_pairs_dict[new_pair1] = amount
                if new_pair2 in new_pairs_dict.keys():
                    new_pairs_dict[new_pair2] = new_pairs_dict[new_pair2] + amount
                else:
                    new_pairs_dict[new_pair2] = amount
                new_pairs_dict[pair] = new_pairs_dict[pair] - amount

                add_char = rule_dict[pair]
                if add_char in element_dict.keys():
                    element_dict[add_char] = element_dict[add_char] + amount
                else:
                    element_dict[add_char] = amount

        pairs_dict = new_pairs_dict

    maximum = max(element_dict.values())
    minimum = min(element_dict.values())
    print(maximum)
    print(minimum)
    return maximum - minimum
    


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

input = utils.get_instructions("fourteen", EXPECTED_LINES)
print(part_one(input, 10))  

print("###########################")
print(part_two(test_input_array)) 
# print(part_two(input)) 
# print(part_one(test_input_array, 40)) 



print("###########################")
print(part_two(input)) 


