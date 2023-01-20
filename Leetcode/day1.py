
def romanToInt(s: str) -> int:
    roman_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    result = 0
    for char in s:
        result += roman_dict[char]
    return result

print(romanToInt(s="MCMXCIV"))