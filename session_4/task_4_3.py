"""
Task 4.3
File data/students.csv stores information about students in CSV format. This file contains the
student’s names, age and average mark.
1. Implement a function which receives file path and returns names of top performer students
def get_top_performers(file_path, number_of_top_students=5):
pass
print(get_top_performers("students.csv"))
>>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
2. Implement a function which receives the file path with srudents info and writes CSV student
information to the new file in descending order of age. Result:

student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""

import csv

def get_top_performers(file_path: str, number_of_top_students = 5) -> list:

    with open(file_path, 'r') as rf:

        reader = csv.DictReader(rf)
        reader = sorted(reader, key = lambda row: float(row['average mark']), reverse = True)
    
    return [row['student name'] for row in reader[ : number_of_top_students]]

def sort_student_by_age(file_path_r: str, file_path_w: str) -> None:

    with open(file_path_r, 'r') as rf, open(file_path_w, 'w') as wf:

        reader = csv.DictReader(rf)

        header = reader.fieldnames
        
        reader = sorted(reader, key = lambda row: int(row['age']), reverse = True)

        writer = csv.DictWriter(wf, fieldnames = header)
        writer.writeheader()
        writer.writerows(reader) 

def main():
    
    file_path = './data/students.csv'

    print(get_top_performers(file_path))
    sort_student_by_age(file_path, './data/sort_students.csv')

if __name__ == '__main__':

    main()