"""
Task 4.1
Open file data/unsorted_names.txt in data folder. Sort the names
and write them to a new file called sorted_names.txt.
Each name should start with a new line as in the following example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(file_path_r: str, file_path_w: str) -> None:
    with open(file_path_r, 'r') as rf, open(file_path_w, 'w') as wf:

        names = rf.readlines()
        names.sort()
        wf.write(''.join(names))


def main():
    sort_names('./data/unsorted_names.txt', './data/sorted_names.txt')


if __name__ == '__main__':
    main()
