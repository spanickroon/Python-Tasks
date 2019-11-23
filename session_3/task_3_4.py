"""
Task 3.4
Implement a function, that receives changeable number of dictionaries
(keys - letters, values - numbers) and combines them into one dictionary.
Dict values should be summarized in case of identical keys
def combine_dicts(*args):
...
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2)
>>> {'a': 300, 'b': 200, 'c': 300}
print(combine_dicts(dict_1, dict_2, dict_3)
>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""

from functools import reduce


def combine_dicts(*args: dict) -> dict:
    d = reduce(lambda x, y: {**x, **y}, args)

    for key in d.keys():
        d[key] = 0
        for i in args:
            if key in i.keys():
                d[key] += i[key]

    return d


def main():
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))


if __name__ == '__main__':
    main()
