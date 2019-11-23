"""
Task 2.1
Implement a function which receives a string and replaces all " symbols with '
and vise versa.
"""


def replacing_qoutes(s: str) -> str:
    return s.translate(s.maketrans({'\'': '\"', '\"': '\''}))


def main():
    print(replacing_qoutes(input()))


if __name__ == '__main__':
    main()
