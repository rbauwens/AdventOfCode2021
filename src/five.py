import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 500


def process_input_part_one(array):
    point_dictionary = dict()
    for i in range(len(array)):  
        start = array[i].split("->")[0]
        end = array[i].split("->")[1]
        x1 = int(start.split(",")[0])
        y1 = int(start.split(",")[1])
        x2 = int(end.split(",")[0])
        y2 = int(end.split(",")[1])
        
        if (x1 != x2) and (y1 != y2):
            # print("skipping, {}".format(array[i]))
            continue
        # print("{}".format(array[i]))
            
        if y1 == y2:
            j = y1
            for i in range(min(x1,x2), max(x1,x2)+1):
                    # print(i, j)
                    if (i,j) not in point_dictionary.keys():
                        point_dictionary[(i, j)] = 1
                    else:
                        point_dictionary[(i, j)] = point_dictionary[(i, j)] + 1
        elif x1 == x2:
            i = x1
            for j in range(min(y1,y2), max(y1,y2)+1):
                    # print(i, j)
                    if (i,j) not in point_dictionary.keys():
                        point_dictionary[(i, j)] = 1
                    else:
                        point_dictionary[(i, j)] = point_dictionary[(i, j)] + 1
    return point_dictionary


def process_input_part_two(array):
    point_dictionary = dict()
    for i in range(len(array)):  
        start = array[i].split("->")[0]
        end = array[i].split("->")[1]
        x1 = int(start.split(",")[0])
        y1 = int(start.split(",")[1])
        x2 = int(end.split(",")[0])
        y2 = int(end.split(",")[1])
        
        # print("{}".format(array[i]))
            
        if y1 == y2:
            j = y1
            for i in range(min(x1,x2), max(x1,x2)+1):
                    if (i,j) not in point_dictionary.keys():
                        point_dictionary[(i, j)] = 1
                    else:
                        point_dictionary[(i, j)] = point_dictionary[(i, j)] + 1
        elif x1 == x2:
            i = x1
            for j in range(min(y1,y2), max(y1,y2)+1):
                    if (i,j) not in point_dictionary.keys():
                        point_dictionary[(i, j)] = 1
                    else:
                        point_dictionary[(i, j)] = point_dictionary[(i, j)] + 1
        else:
            # diagonal line
            if x1 > x2:
                start_x = x2
                end_x = x1
                start_y = y2
                end_y = y1
            else:
                start_x = x1
                end_x = x2
                start_y = y1
                end_y = y2
            y_decreasing = False
            if end_y < start_y:
                y_decreasing = True
            difference = (end_x - start_x) + 1
            i = start_x
            j = start_y
            for k in range(0, difference):
                if (i,j) not in point_dictionary.keys():
                    point_dictionary[(i, j)] = 1
                else:
                    point_dictionary[(i, j)] = point_dictionary[(i, j)] + 1
                i = i + 1
                if y_decreasing:
                    j = j - 1
                else:
                    j = j + 1



    return point_dictionary


def get_result(map):
    total = 0
    for key in map.keys():
        if map[key] > 1:
            total = total + 1
    return total

def part_one(array):
    map = process_input_part_one(array)
    return get_result(map)
 
        

def part_two(array):
    map = process_input_part_two(array)
    return get_result(map)



test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array)) 

print("###########################")

input = utils.get_instructions("five", EXPECTED_LINES)
print(part_one(input)) 

print("###########################")

print(part_two(test_input_array))

print("###########################")

print(part_two(input)) 


