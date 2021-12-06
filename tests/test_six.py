import pytest
import src.six as day

# python -m pytest ..\tests\test_template.py -s

example_input = day.test_input_array
real_input = day.input

def test_example_part_one():
    assert 26 == day.part_one(day.test_input_array.copy(), 18)

def test_example_part_one_eighty():
    assert 5934 == day.part_one(day.test_input_array.copy(), 80)

def test_example_part_two():
    assert 26984457539 == day.part_two(day.test_input_array.copy(), 256)


def test_part_one():
    assert 375482 == day.part_one(day.input.copy(), 80)


def test_part_two():
    assert 1689540415957 == day.part_two(day.input.copy(), 256)

