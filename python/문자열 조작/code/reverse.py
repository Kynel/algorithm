from typing import List


def reverseString(s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1


if __name__ == "__main__":
    input = list(f"input string!")
    print(input)
    reverseString(input)
    print(input)
