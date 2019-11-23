"""
Task 4.5
Implement a decorator remember_result which remembers last result of function
it decorates
and prints it before next call.

@remember_result
def sum_list(*args):
result = ""
for item in args:
result += item
print(f"Current result = '{result}'")
return result
sum_list("a", "b")
>>> "Last result = 'None'"
>>> "Current result = 'ab'"
sum_list("abc", "cde")
>>> "Last result = 'ab'"
>>> "Current result = 'abccde'"
sum_list(3, 4, 5)
>>> "Last result = 'abccde'"
>>> "Current result = '12'"
"""

from functools import reduce


def remember_result(func):
    last_res = None

    def wrapper(*args, **kwargs):
        nonlocal last_res

        print(f'Last result: {last_res}')
        last_res = func(*args, **kwargs)

        return last_res
    return wrapper


@remember_result
def sum_list(*args):
    res = reduce(lambda x, y: x + y, args)
    print(f'Current result: {res}\n')

    return res


def main():
    sum_list(1, 1)
    sum_list('kek', 'lol')
    sum_list(3, 3)


if __name__ == '__main__':
    main()
