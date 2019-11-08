"""
Task 4.2
Implement a function which search for most common words in the file. Use
data/lorem_ipsum.txt file as a example.

def most_common_words(filepath, number_of_words=3):
pass
print(most_common_words('lorem_ipsum.txt'))
>>> ['donec', 'etiam', 'aliquam']
NOTE: Remember about dots, commas, capital letters etc.
"""

from collections import Counter

def most_common_worlds(file_path: str, number_of_words = 3) -> list:

    with open(file_path) as rf:

        words = rf.read()
        words = Counter(list(filter(str.isalpha, str.lower(words).split())))

    return [i[0] for i in words.most_common(number_of_words)]

def main():

    print(most_common_worlds('./data/lorem_ipsum.txt'))

if __name__ == '__main__':
    main()