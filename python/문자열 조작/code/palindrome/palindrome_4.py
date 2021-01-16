import re


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]


if __name__ == "__main__":
    input = f"A man, a plan, a canal: Panama"
    print(isPalindrome(input))
