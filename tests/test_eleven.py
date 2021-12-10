import pytest
import src.eleven as day

# python -m pytest ..\tests\test_template.py -s

example_input = day.test_input_array
real_input = day.input

def test_example_part_one():
    assert 26397 == day.part_one(example_input)

def test_example_part_two():
    assert 288957 == day.part_two(example_input)


def test_part_one():
    assert 411471 == day.part_one(real_input)


def test_part_two():
    assert 3122628974 == day.part_two(real_input)
