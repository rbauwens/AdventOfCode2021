import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils



EXPECTED_LINES = 200
           
    
def part_one(array):
    unique_lengths = [2,3,4,7]
    unique = 0
    for line in array:
        second_part = line.split(" | ")[1]
        for entry in second_part.split(" "):
            if len(entry) in unique_lengths:
                unique = unique + 1
    return unique

def get_sum(line):
    unique_lengths = [2,3,4,7]
    num_dict = dict()

    # first pass
    for entry in line.split(" "):
        # if entry.contains("|"):
        if "|" in entry:
            continue
        if len(entry) == 2:
            num_dict[1] = entry
        elif len(entry) == 3:
            num_dict[7] = entry
        elif len(entry) == 4:
            num_dict[4] = entry
        elif len(entry) == 7:
            num_dict[8] = entry
    
    # second pass
    for entry in line.split(" "):
        # if entry.contains("|"):
        if "|" in entry:
            continue
        if len(entry) in unique_lengths:
            continue
        elif len(entry) == 5:
            # 2, 3, 5
            num = two_three_or_five(entry, num_dict)
            num_dict[num] = entry
        elif len(entry) == 6:
            # 0, 6, 9
            num = zero_six_or_nine(entry, num_dict)
            num_dict[num] = entry
        else: 
            print("UNKNOWN NUMBER")
            return
    
    total = compute_final_sum(num_dict, line)
    # print(total)
    return total


def compute_final_sum(num_dict, line):
    second_part = line.split(" | ")[1]
    nums = second_part.split(" ")
    total = ""
    for num in nums:
        for key in num_dict.keys():
            if set(num_dict[key]) == set(num):
                total = total + str(key)
    return total



def two_three_or_five(entry, num_dict):
    is_three = True
    for letter in num_dict[1]:
        if letter not in entry:
            is_three = False
    if is_three:
        return 3
    four = num_dict[4]
    one = num_dict[1]
    five_part_of_four = ""
    for letter in four:
        if letter not in one:
            five_part_of_four = five_part_of_four + letter
    
    is_five = True
    for letter in five_part_of_four:
        if letter not in entry:
            is_five = False
    if is_five:
        return 5
    return 2

# got 1, 4, 7, 8
def zero_six_or_nine(entry, num_dict):
    is_nine = True
    for letter in num_dict[4]:
        if letter not in entry:
            is_nine = False
    if is_nine:
        return 9

    is_zero = True
    for letter in num_dict[1]:
        if letter not in entry:
            is_zero = False
    if is_zero:
        return 0
    
    return 6



def part_two(array):
    unique_lengths = [2,3,4,7]
    total_sum = 0
    for line in array:
        sum = get_sum(line)
        total_sum = total_sum + int(sum)
        
    return total_sum




test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
test_input_array = test_input.split("\n")
# test_input_array = test_input.split(" ")


print(part_one(test_input_array)) 

print("###########################")

input = utils.get_instructions("eight", EXPECTED_LINES)
print(part_one(input)) 


print("###########################")

print(part_two(test_input_array))


print("###########################")

print(part_two(input)) 



