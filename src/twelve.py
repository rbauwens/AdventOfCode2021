import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 22

def get_dict(array):
    my_dict = dict()
    for line in array:
        start = line.split("-")[0]
        end = line.split("-")[1]
        if start not in my_dict.keys():
            my_dict[start] = [end]
        else:
            my_dict[start].append(end)
        if end not in my_dict.keys():
            my_dict[end] = [start]
        else:
            my_dict[end].append(start)
    return my_dict

def get_routes(paths):
    pos = 'start'
    routes = []
    for loc in paths[pos]:
        routes.append([pos, loc])

    change = True
    while change:
        change = False
        for route in routes:
            
            pos = route[-1]
            if pos == 'end':
                continue
            if len(paths[pos]) == 1:
                loc = paths[pos][0]
                if loc.islower() and loc in route:
                    continue
                # if pos.islower() and (loc != 'end'):
                #     continue
                if pos.islower() and (len(paths[loc]) == 1) and (loc != 'end'):
                    continue
                route.append(loc)
                change = True
            else:
                for loc in paths[pos]:
                    if loc.islower() and loc in route:
                        continue
                    # if pos.islower() and (loc != 'end'):
                    #     continue
                    if pos.islower() and (len(paths[loc]) == 1) and (loc != 'end'):
                        continue
                    new_route = route.copy()
                    new_route.append(loc)
                    routes.append(new_route)
                    change = True
                routes.remove(route)

    for route in routes:
        if route[-1] != 'end':
            routes.remove(route)
    return routes

def is_duplicate_done(route):
    for char in route:
        if char.isupper():
            continue
        count = route.count(char)
        if count > 1:
            return True
    return False

def get_routes_p2(paths):
    pos = 'start'
    routes = []
    for loc in paths[pos]:
        routes.append([pos, loc])

    change = True
    while change:
        change = False
        for route in routes:
            duplicate_done = is_duplicate_done(route)
            pos = route[-1]
            if pos == 'end':
                continue
            if len(paths[pos]) == 1:
                loc = paths[pos][0]
                if duplicate_done:
                    if pos.islower() and (len(paths[loc]) == 1) and (loc != 'end'):
                        continue
                if loc.islower():
                    if loc in route:
                        if duplicate_done or loc == 'start' or loc == 'end':
                            continue
                        duplicate_done = True
                
                route.append(loc)
                change = True
            else:
                for loc in paths[pos]:
                    new_route = route.copy()
                    duplicate_done = is_duplicate_done(new_route)
                    if duplicate_done:
                        if pos.islower() and (len(paths[loc]) == 1) and (loc != 'end'):
                            continue
                    if loc.islower():
                        if loc in route:
                            if duplicate_done or loc == 'start' or loc == 'end':
                                continue
                            duplicate_done = True
                    
                    
                    new_route.append(loc)
                    routes.append(new_route)
                    change = True
                routes.remove(route)

    for route in routes:
        if route[-1] != 'end':
            routes.remove(route)
    return routes

def part_one(array, part_two = False):
    paths = get_dict(array)
    if part_two:
        routes = get_routes_p2(paths)
        # for route in routes:
        #     print(route)
    else:
        routes = get_routes(paths)
    
    return len(routes)

def part_two(array):
    return


test_input_one = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
test_input_array_one = test_input_one.split("\n")
print("Test 1")
print(part_one(test_input_array_one)) 

print("Test 2")
test_input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
test_input_array2 = test_input2.split("\n")
print(part_one(test_input_array2)) 

print("Test 3")
test_input3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
test_input_array3 = test_input3.split("\n")
print(part_one(test_input_array3)) 

print("###########################")

input = utils.get_instructions("twelve", EXPECTED_LINES)
print(part_one(input)) 

print("###########################")
print(part_one(test_input_array_one, part_two=True)) 
print(part_one(test_input_array2, part_two=True)) 
print(part_one(test_input_array3, part_two=True)) 

print("###########################")

print(part_one(input, part_two=True)) 

