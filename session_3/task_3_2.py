"""
Task 3.2
Implement a function that takes a number as an argument and returns
a dictionary, where the key is a number and the value is the square
of that number.
print(generate_squares(5))
>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


def generate_squares(n: int) -> dict:
    return {i: i ** 2 for i in range(1, n + 1)}


def main():
    print(generate_squares(5))


if __name__ == '__main__':
    main()
