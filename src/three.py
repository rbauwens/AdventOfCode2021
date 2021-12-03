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
    mydict = dict()
    for j in range(len(array[0])):  
        mydict[j] = []
        for i in range(len(array)):  
            mydict[j].append(array[i][j])
        
    most_freq = []
    for k in mydict.keys():
        most_freq.append(most_frequent(mydict[k]))
        
    # print("most_freq {}".format(most_freq))
    least_freq = []
    for i in range(len(most_freq)):
        if most_freq[i] == '0':
            least_freq.append('1')
        elif most_freq[i] == '1':
            least_freq.append('0')
    # print("least_freq {}".format(least_freq))

    most_freq_string = ''.join(most_freq)
    least_freq_string = ''.join(least_freq)
    mf_int = int(most_freq_string, 2)
    lf_int = int(least_freq_string, 2)
    # print("mf_int", mf_int)
    # print("lf_int", lf_int)
    return mf_int * lf_int
         

def part_two_compute(array, select_most_frequent = True):
    mydict = dict() 
    for j in range(len(array[0])):  
        # print("iteration {}".format(j))
        # print("    LEN:", len(array))
        mydict[j] = []
        for i in range(len(array)):  
            mydict[j].append(array[i][j])

        most_freq = []
        for k in mydict.keys():
            most_freq.append(most_frequent(mydict[k]))        
        one_count = mydict[j].count('1')
        zero_count = mydict[j].count('0')
        
        if select_most_frequent:
            select = '1'
            if zero_count > one_count:
                select = '0'
        else:
            select = '0'
            if one_count < zero_count:
                select = '1'
        # print("    select {}".format(select))
        
        remove = []
        for i in range(len(array)):  
            if array[i][j] != select:
                remove.append(i)
        tmp_array = array.copy()
        for i in remove:
            array.remove(tmp_array[i])
        
        # print("    LEN:", len(array))
        if len(array) == 1:
            return array



def part_two(array):
    
    oxygen = part_two_compute(array.copy(), select_most_frequent=True)
    carbon = part_two_compute(array.copy(), select_most_frequent=False)
    
    print("oxygen, carbon")
    print(oxygen, carbon)
    ox_string = ''.join(oxygen)
    co2_string = ''.join(carbon)
    ox_int = int(ox_string, 2)
    co2_int = int(co2_string, 2)
    print(ox_int, co2_int)
    return ox_int * co2_int




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

print(part_one(test_input_array)) #198
print("###########################")
input = utils.get_instructions("three", EXPECTED_LINES)

#2595824
print(part_one(input)) 

print("###########################")
# 230
print(part_two(test_input_array))
print("###########################")

#2135254
print(part_two(input)) 

