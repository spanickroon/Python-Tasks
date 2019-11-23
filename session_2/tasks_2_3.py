"""
Task 2.3
Implement a function which works the same as str.split method
(without using str.split itself, ofcourse).
"""


def my_split(s: str) -> str:
    res = []
    temp = []

    for i in list(s):
        if i != ' ':
            temp.append(i)
        else:
            res.append(''.join(temp))
            temp.clear()

    res.append(res.append(''.join(temp)))

    return list(filter(None, res))


def main():
    print(my_split(input()))


if __name__ == '__main__':
    main()
