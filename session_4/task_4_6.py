"""
Task 4.6
Implement a decorator call_once which runs a function or method once.

@call_once
def sum_of_numbers(a, b):
return a + b
print(sum_of_numbers(13, 42))
>>> 55
sum_of_numbers(13, 42)
sum_of_numbers(13, 42)
sum_of_numbers(13, 42)
"""


def call_once(func):
    calls = 0

    def wrapper(a, b):
        nonlocal calls
        calls += 1

        return func(a, b) if calls < 2 else None
    return wrapper


@call_once
def sum_of_numbers(a, b):
    print(a + b)
    return a + b


def main():
    sum_of_numbers(13, 42)
    sum_of_numbers(13, 42)
    sum_of_numbers(13, 42)


if __name__ == '__main__':
    main()
