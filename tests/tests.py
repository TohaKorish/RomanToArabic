import pytest as pytest

from src.roman_to_arabic import roman_to_arabic


@pytest.mark.parametrize("roman, arabic", [
    ('I', 1), ('II', 2), ('III', 3), ('IV', 4), ('V', 5), ('VI', 6), ('VII', 7), ('VIII', 8),
    ('IX', 9), ('X', 10), ('XI', 11), ('XX', 20), ('XXX', 30), ('XL', 40), ('L', 50),
    ('LX', 60), ('XC', 90), ('C', 100), ('CD', 400), ('D', 500), ('DC', 600), ('CM', 900),
    ('M', 1000), ('MM', 2000), ('MMM', 3000), ('MMMM', 4000)
])
def test_roman_to_arabic_conversion(roman, arabic):
    assert roman_to_arabic(roman) == arabic


def test_empty_input():
    with pytest.raises(ValueError):
        roman_to_arabic('')


def test_lower_case_input():
    assert roman_to_arabic("ix") == 9


def test_mixed_case_input():
    assert roman_to_arabic("mCmXcIv") == 1994


def test_invalid_roman_input():
    with pytest.raises(ValueError):
        roman_to_arabic('DM')
    with pytest.raises(ValueError):
        roman_to_arabic('VIV')
    with pytest.raises(ValueError):
        roman_to_arabic('MMMXM')


def test_whitespace_within_numerals():
    with pytest.raises(ValueError):
        roman_to_arabic("I X")


@pytest.mark.parametrize("string", ['r', 'ea', '54'])
def test_invalid_string_input(string):
    with pytest.raises(ValueError):
        roman_to_arabic(string)


def test_invalid_digit_type():
    with pytest.raises(TypeError):
        roman_to_arabic(123)


def test_value_with_space():
    with pytest.raises(ValueError):
        roman_to_arabic(' X')


def test_invalid_dict_type():
    with pytest.raises(TypeError):
        roman_to_arabic(['X', 'I'])
