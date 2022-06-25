"""
Napisz funkcje sprawdzającą czy dane słowo jest palindromem
Hint: Palindrom to słowo brzmiące od przodu jak i od tyłu tak samo
"""


def is_palindrome(text):
    text = "".join(text.lower().split())
    return text == text[::-1]



assert is_palindrome("ala") == True
assert is_palindrome("Oka") == False
assert is_palindrome("OkO") == True
assert is_palindrome("A to idiOta") == True
#assert is_palindrome("A to idiota!") == True


