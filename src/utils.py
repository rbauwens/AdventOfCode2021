import os
import sys 

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')



def get_instructions(day, expected_lines):
    
    data_file = os.path.join(DATA_FOLDER, 'day_{}_data'.format(day))

    instructions = []
    with open(data_file) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(int(line.strip()))
            line = fp.readline()
            lines_read += 1

    if (lines_read != expected_lines + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions