"""
Task 2.2
Write a function that check whether a string is a palindrome or not. Usage of any reversing
functions is prohibited. To check your implementation you can use strings from here.
"""

def palindrome(s: str) -> str:

    return s == s[::-1]

def main():

    print(palindrome(input()))

if __name__ == '__main__':

    main()