"""
Task 2.5
Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given
integer's digits. Example:
>>> split_by_index(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
"""

def split_by_index(s: str) -> tuple:

    return tuple(map(int, list(str(s))))

def main():

    print(split_by_index(input()))

if __name__ == '__main__':

    main()