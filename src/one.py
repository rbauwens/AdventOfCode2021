import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 200


def dayone_function(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if (array[i] + array[j] == 2020):
                return array[i] * array[j]


def dayone_function_p2(array):
  for i in range(len(array)):
      for j in range(len(array)):
        for k in range(len(array)):
          if (array[i] + array[j] + array[k] == 2020):
              return array[i] * array[j] * array[k]



dayone_partone_input = utils.get_instructions("one", EXPECTED_LINES)
print(dayone_function(dayone_partone_input))

print(dayone_function_p2(dayone_partone_input))
