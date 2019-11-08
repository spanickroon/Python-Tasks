"""
Task 2.4
Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits
the s string by indexes specified in indexes . Wrong indexes must be ignored. Examples:

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]
>>> split_by_index("no luck", [42])
["no luck"]
"""

def split_by_index(s: str, arr: list) -> list:

    arr = list(filter(lambda x: x < len(s) or x > 0, arr))
    i = 1

    while (i < len(arr)):
    
        if arr[i] <= arr[i - 1]:
            del arr[i]
            i -= 1
        else:
            i += 1

    arr.insert(0,0)
    arr.append(len(s))
    
    return [s[i:j] for i, j in zip(arr, arr[1:])]

def main():

    print(split_by_index('pythoniscool,isn\'tit?', [6, 8, 12, 13, 18]))

if __name__ == '__main__':
    
    main()