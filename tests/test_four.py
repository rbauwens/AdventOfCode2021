import pytest
import src.four as day

# python -m pytest ..\tests\test_template.py -s

example_input = day.test_input_array
real_input = day.input

def test_example_part_one():
    assert 198 == day.part_one(example_input)

def test_example_part_two():
    assert 230 == day.part_two(example_input)


def test_part_one():
    assert 2595824 == day.part_one(real_input)


def test_part_two():
    assert 2135254 == day.part_two(real_input)
