import pytest
import src.one as one

# python -m pytest ..\tests\test_template.py -s
test_input = """199
200
208
210
200
207
240
269
260
263"""
example_input = test_input.split("\n")

day_one_input = one.input

def test_example_part_one():
    assert 7 == one.part_one(example_input)

def test_example_part_two():
    assert 5 == one.part_two(example_input)


def test_part_one():
    assert 1121 == one.part_one(day_one_input)


def test_part_two():
    assert 1065 == one.part_two(day_one_input)
