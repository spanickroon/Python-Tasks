"""
Task 3.3
Implement a function, that takes string as an argument and returns
a dictionary, that contains letters of given string as keys
and a number of their occurrence as values.
print(count_letters("stringsample"))
>>> {'s': 2, 't': 1, 'r': 1, 'i': 1,
'n': 1, 'g': 1, 'a': 1, 'm': 1,
'p': 1, 'l': 1, 'e': 1}
"""


def count_letters(s: str) -> dict:
    return {i: s.count(i) for i in s}


def main():
    print(count_letters(input()))


if __name__ == '__main__':
    main()
