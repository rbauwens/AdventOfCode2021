import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 601

def process_line(current_dict, row, line):
    nums = line.split(' ')
    col = 0
    for i in range(len(nums)):
        if nums[i] != '':
            current_dict[(row, col)] = [nums[i], False]
            col = col + 1
    return current_dict
    

def process_input(array):
    numbers_called = array[0]
    boards = []
    next_dict = dict()
    row = 0
    for i in range(1, len(array)):
        if array[i] == '':
            if len(next_dict.keys()) == 25:
                boards.append(next_dict)
                next_dict = dict()
                row = 0
        else:
            next_dict = process_line(next_dict, row, array[i])
            row = row + 1
    if len(next_dict.keys()) == 25:
        boards.append(next_dict)
    return numbers_called, boards
        

def mark_number(board, number):
    for value in board.values():
        if value[0] == number:
            value[1] = True
            return

def is_board_winner(board):
    for row in range(0,5):
        if (board[(row, 0)][1] == True) and (board[(row, 1)][1] == True) and (board[(row, 2)][1] == True) \
            and (board[(row, 3)][1] == True) and (board[(row, 4)][1] == True):
            return True
    for column in range(0,5):
        if (board[(0, column)][1] == True) and (board[(1, column)][1] == True) and (board[(2, column)][1] == True) \
            and (board[(3, column)][1] == True) and (board[(4, column)][1] == True):
            return True
    return False

def calculate_score(board, number):
    sum = 0
    for row in range(0,5):
        for column in range(0,5):
            if board[(row, column)][1] == False:
                sum = sum + int(board[(row, column)][0])
    return sum * int(number)

def part_one(array):
    numbers_called, boards = process_input(array)
    is_winner = []
    numbers_called = numbers_called.split(',')
    for number in numbers_called:
        for board in boards:
            mark_number(board, number)
            winner = is_board_winner(board)
            if winner:
                is_winner.append(board)
        if len(is_winner) > 0:
            print("WINNER")
            if len(is_winner) != 1:
                return Exception("too many winners")
            return calculate_score(is_winner[0], number)


def part_two(array):
    numbers_called, boards = process_input(array)
    is_winner = []
    numbers_called = numbers_called.split(',')
    num_boards = len(boards)
    for number in numbers_called:
        for board in boards:
            mark_number(board, number)
            winner = is_board_winner(board)
            if winner:
                if board not in is_winner:
                    is_winner.append(board)
        if len(is_winner) == num_boards - 1:
            print("ONE BOARD REMAINING")
            for board in boards:
                if board not in is_winner:
                    last_board = board        
        if len(is_winner) == num_boards:
            return calculate_score(last_board, number)

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array)) 

print("###########################")

input = utils.get_instructions("four", EXPECTED_LINES)
print(part_one(input)) 

print("###########################")

print(part_two(test_input_array))

print("###########################")

print(part_two(input)) 

