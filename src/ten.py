import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 106

def is_match(char2, char1):
    if char1 == '[':
        if char2 != ']':
            return False
    elif char1 == '(':
        if char2 != ')':
            return False
    if char1 == '<':
        if char2 != '>':
            return False
    if char1 == '{':
        if char2 != '}':
            return False
    return True

def get_illegal(line):
    openers = ["[", "(", "{", "<"]
    closers = ["]", ")", "}", ">"]
    illegals = []
    current_openers = []
    for char in line:
        if char in openers:
            current_openers.append(char)
        if char in closers:
            if not is_match(char, current_openers[-1]):
                illegals.append(char)
                # print(line)
                return char
            else:
                current_openers.pop()
    return None

def incomplete(line):
    openers = ["[", "(", "{", "<"]
    closers = ["]", ")", "}", ">"]
    illegals = []
    current_openers = []
    for char in line:
        if char in openers:
            current_openers.append(char)
        if char in closers:
            if not is_match(char, current_openers[-1]):
                illegals.append(char)
                # print(line)
                return False, None
            else:
                current_openers.pop()
    if len(current_openers) != 0:
        return True, current_openers
    else:
        return False, None

def lookup(illegal):
    if illegal == ')':
        return 3
    elif illegal == ']':
        return 57
    elif illegal == '}':
        return 1197
    elif illegal == '>':
        return 25137

def get_p2_value(illegal):
    if illegal == ')':
        return 1
    elif illegal == ']':
        return 2
    elif illegal == '}':
        return 3
    elif illegal == '>':
        return 4

def get_completion(current_openers):
    closing = []
    for opening in current_openers:
        if opening == '(':
            closing.append(')')
        elif opening == '[':
            closing.append(']')
        elif opening == '{':
            closing.append('}')
        elif opening == '<':
            closing.append('>')
    
    closing.reverse()
    return closing

def get_value(string):
    total = 0
    for char in string:
        add = get_p2_value(char)
        total = (5 * total) + add
    return total

def part_one(array):
    total_value = 0
    for line in array:  
        illegal = get_illegal(line)
        if illegal is not None:
            value = lookup(illegal)
            total_value = total_value + value
            
    return total_value

def part_two(array):
    total_values = []
    for line in array:
        is_incomplete, current_openers = incomplete(line)
        if is_incomplete:
            string = get_completion(current_openers)
            value = get_value(string)
            total_values.append(value)
    total_values.sort()
    middle = math.floor(len(total_values) / 2) 
    return total_values[middle]



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

