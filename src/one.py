import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 2000


def dayone_function(array):
    
  num_increased = 0
  for i in range(len(array)):  
    if i == 0:
      pass
    else:
      if array[i]>array[i-1]:
        num_increased = num_increased + 1
  return num_increased
        

def dayone_function_p2(array):
  windows = []
  for i in range(len(array)):  
    if i == 0 or i == 1:
      pass
    else:
      windows.append(array[i] + array[i-1] + array[i-2])
        
  return dayone_function(windows)


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
dayone_partone_input = utils.get_instructions("one", EXPECTED_LINES)
print(dayone_function(test_input_array))
# print(dayone_function(dayone_partone_input))

print(dayone_function_p2(test_input_array))
print(dayone_function_p2(dayone_partone_input))
