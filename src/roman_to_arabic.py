def roman_to_arabic(roman):
    for char in roman:
        if char.isspace():
            raise ValueError("Invalid character")
    if not isinstance(roman, str):
        raise TypeError("Input must be a string")
    if len(roman) == 0:
        raise ValueError("Input must have at least one character")
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    arabic = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_numerals.get(char.upper())
        if value is None:
            raise ValueError("Invalid Roman numeral")

        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        prev_value = value

    return arabic
