import pytest
import src.five as day

# python -m pytest ..\tests\test_template.py -s

example_input = day.test_input_array
real_input = day.input

def test_example_part_one():
    assert 4512 == day.part_one(example_input)

def test_example_part_two():
    assert 1924 == day.part_two(example_input)


def test_part_one():
    assert 39984 == day.part_one(real_input)


def test_part_two():
    assert 8468 == day.part_two(real_input)
