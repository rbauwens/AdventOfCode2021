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
            instructions.append(line.strip())
            line = fp.readline()
            lines_read += 1

    if (lines_read != expected_lines + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions

# Use this when the fill instruction line is a single int
def get_instructions_int(day, expected_lines):
    
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

def get_instructions_single_line(day, expected_lines):
    
    data_file = os.path.join(DATA_FOLDER, 'day_{}_data'.format(day))

    instructions = []
    with open(data_file) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(line.strip())
            line = fp.readline()
            lines_read += 1

    if (lines_read != expected_lines + 1):
        sys.exit("Did not read the correct amount of lines")

    take = instructions[0]
    new = take.split(',')

    return new