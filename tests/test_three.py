import pytest
import src.two as two

# python -m pytest ..\tests\test_template.py -s

example_input = two.test_input_array
day_one_input = two.input

def test_example_part_one():
    assert 150 == two.part_one(example_input)

def test_example_part_two():
    assert 900 == two.part_two(example_input)


def test_part_one():
    assert 2117664 == two.part_one(day_one_input)


def test_part_two():
    assert 2073416724 == two.part_two(day_one_input)
