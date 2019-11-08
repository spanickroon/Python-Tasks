"""
Task 3.1
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1. characters that appear in all strings
2. characters that appear in at least one string
3. characters that appear at least in two strings
4. characters of alphabet, that were not used in any string
Note: use string.ascii_lowercase for list of alphabet letters

test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
>>> {'o'}
print(test_1_2(*strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
"""

from functools import reduce
from string import ascii_lowercase

def test_1_1(*s: str) -> dict:
    
    return reduce(lambda x, y: x & y, [set(i) for i in s])

def test_1_2(*s: str) -> dict:

    return reduce(lambda x, y: x | y, [set(i) for i in s])

def test_1_3(*s: str) -> dict:

    res = []

    for i in s:

        res.append(set(i) & reduce(lambda x, y: x | y, [set(j) for j in s[:s.index(i)] + s[s.index(i) + 1:]]))

    return reduce(lambda x, y: x | y, [i for i in res])

def test_1_4(*s: str) -> str:
    
    return set(ascii_lowercase) - test_1_2(*s)

def main():

    print(test_1_1('hello','world','python'))
    print(test_1_2('hello','world','python'))
    print(test_1_3('world','hello','python'))
    print(test_1_4('hello','world','python'))

if __name__ == '__main__':
    
    main()