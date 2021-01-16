def isPalindrom(s: str) -> bool:
    s_len = len(s) // 2

    for i in range(s_len):
        if(s[i] != s[-(i+1)]):
            return False

    return True


if __name__ == "__main__":
    input = f"aaaaaaaaaaaaaaaaaaaaaa"
    print(isPalindrom(input))
