import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 1000

from collections import Counter
 
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]
   


def part_one(array):
    list_of_lists = []
    mydict = dict()
    for j in range(len(array[0])):  
        mydict[j] = []
        for i in range(len(array)):  
            mydict[j].append(array[i][j])
        
    most_freq = []
    for k in mydict.keys():
        most_freq.append(most_frequent(mydict[k]))
        
    print("most_freq {}".format(most_freq))
    least_freq = []
    for i in range(len(most_freq)):
        if most_freq[i] == '0':
            least_freq.append('1')
        elif most_freq[i] == '1':
            least_freq.append('0')
    print("least_freq {}".format(least_freq))

    most_freq_string = ''.join(most_freq)
    least_freq_string = ''.join(least_freq)
    str1 = ''.join(str(e) for e in least_freq)
    mf_int = int(most_freq_string, 2)
    lf_int = int(least_freq_string, 2)
    print("mf_int", mf_int)
    print("lf_int", lf_int)
    return mf_int * lf_int


    

        
    

    return 
  
        

def part_two(array):
    return



test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))
# print("###########################")
input = utils.get_instructions("three", EXPECTED_LINES)

print(part_one(input))

# print("###########################")

# print(part_two(test_input_array))
# print(part_two(input))


