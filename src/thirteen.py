import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 828

def process_input(array):
    dot_map = dict()
    next = False
    next2 = False
    #down
    max_i = 0
    #across
    max_j = 0
    folds = []
    for line in array:
        if next:
            folds.append(line)
            # fold_one = line
            # next = False
            # next2 = True
        # elif next2:
            # fold_two = line
            # next2 = False
        elif line == '':
            next = True
        else:
            j = int(line.split(",")[0])
            i = int(line.split(",")[1])
            if i > max_i:
                max_i = i
            if j > max_j:
                max_j = j
            dot_map[(i, j)] = '#'
    for down in range(max_i + 1):
        for across in range(max_j + 1):
            if (down, across) in dot_map.keys():
                continue
            else:
                dot_map[(down, across)] = '.'
    
    return dot_map, folds

def get_max(dot_map):
    max_i = 0
    max_j = 0
    for key in dot_map.keys():
        if key[0] > max_i:
            max_i = key[0]
        if key[1] > max_j:
            max_j = key[1]
    # return max_i+1, max_j+1
    return max_i, max_j

def do_fold(dot_map, fold):
    
    max_i, max_j = get_max(dot_map)
    
    
    line = fold.split(" ")[2]
    line_num = int(line.split("=")[1])
    print(max_i, max_j, line)
    dir = line.split("=")[0]
    if dir == "y":
        direction = "Horizontal"
    if dir == "x":
        direction = "Vertical"
    new_map = dict()
    if direction == 'Horizontal':
        for i in range(line_num):
            # print(i, line_num)
            # print(line_num - i - 1)
            # print(line_num + i + 1)
            for across in range(max_j+1):
                if (i+ line_num + 1) > max_i:
                    new_map[((line_num - i -1), across)] = '.'
                    continue
                
                if (dot_map[((line_num - i -1), across)] == '.') and (dot_map[((i+ line_num + 1), across)] == '.'):
                    new_map[((line_num - i -1), across)] = '.'
                elif (dot_map[((line_num - i -1), across)] == '#') and (dot_map[((i+ line_num + 1), across)] == '.'):
                    new_map[((line_num - i -1), across)] = '#'
                elif (dot_map[((line_num - i -1), across)] == '.') and (dot_map[((i+ line_num + 1), across)] == '#'):
                    new_map[((line_num - i -1), across)] = '#'
                elif (dot_map[((line_num - i -1), across)] == '#') and (dot_map[((i+ line_num + 1), across)] == '#'):
                    new_map[((line_num - i -1), across)] = '#'


    if direction == 'Vertical':
        for i in range(max_i+1):
            # print(i, line_num)
            
            for across in range(line_num):
                if (line_num + across + 1) > max_j:
                    new_map[(i, line_num - across - 1)] = '.'
                    continue
                # print('###############') 
                # print([(i, line_num - across - 1)])
                # print([(i, line_num + across + 1)])   
                # print('###############') 
                if (dot_map[(i, line_num - across - 1)] == '.') and (dot_map[(i, line_num + across + 1)] == '.'):
                    new_map[(i, line_num - across - 1)] = '.'
                elif (dot_map[(i, line_num - across - 1)] == '#') and (dot_map[(i, line_num + across + 1)] == '.'):
                    new_map[(i, line_num - across - 1)] = '#'
                elif (dot_map[(i, line_num - across - 1)] == '.') and (dot_map[(i, line_num + across + 1)] == '#'):
                    new_map[(i, line_num - across - 1)] = '#'
                elif (dot_map[(i, line_num - across - 1)] == '#') and (dot_map[(i, line_num + across + 1)] == '#'):
                    new_map[(i, line_num - across - 1)] = '#'
    dots = 0
    for key in new_map.keys():
        if new_map[key] == '#':
            dots = dots + 1
    return dots, new_map

def print_map(new_map):
    max_i, max_j = get_max(new_map)
    for i in range(max_i+1):
        e = ""
        for j in range(max_j+1):
            e = e + (new_map[i, j])
        print(e)

def part_one(array):
    dot_map, folds = process_input(array)
    dots, new_map = do_fold(dot_map, folds[0])
    print("fold 1: ", dots)
    # print_map(new_map)
    # dots2, new_map2 = do_fold(new_map, folds[1], max_i,  max_j)
    # print("fold 2: ", dots2)
    # print_map(new_map2)
    return dots

def part_two(array):
    dot_map, folds = process_input(array)
    for fold in folds:
        dots, new_map = do_fold(dot_map, fold)
        dot_map = new_map
        print("fold: ", dots)
        # print_map(new_map)
        # dots2, new_map2 = do_fold(new_map, folds[1], max_i,  max_j)
        # print("fold 2: ", dots2)
    print_map(new_map)
    print("ANSWER")
    return dots


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

print(part_one(test_input_array)) #17

print("###########################")

input = utils.get_instructions("thirteen", EXPECTED_LINES)
print(part_one(input))  #693

print("###########################")
print(part_two(test_input_array)) 


print("###########################")
print(part_two(input)) #95
# UCLZRAZU

