import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 2000


def part_one(array):
    
  num_increased = 0
  for i in range(len(array)):  
    if i == 0:
      pass
    else:
      if array[i]>array[i-1]:
        num_increased = num_increased + 1
  return int(num_increased)
        

def part_two(array):
  windows = []
  for i in range(len(array)):  
    if i == 0 or i == 1:
      pass
    else:
      windows.append(array[i] + array[i-1] + array[i-2])
        
  return part_one(windows)


test_input = """199
200
208
210
200
207
240
269
260
263"""
test_input_array = test_input.split("\n")
input = utils.get_instructions_int("one", EXPECTED_LINES)
print(part_one(test_input_array))
print(part_one(input))

print(part_two(test_input_array))
print(part_two(input))
