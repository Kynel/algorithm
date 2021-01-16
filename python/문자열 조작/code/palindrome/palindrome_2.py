def preprocess(s: str) -> str:
    result = []
    for char in s:
        if char.isalnum():
            result.append(char.lower())

    return result


def isPalindrom(s: str) -> bool:
    s_len = len(s) // 2

    for i in range(s_len):
        if(s[i] != s[-(i+1)]):
            return False

    return True


if __name__ == "__main__":
    input = f"A man, a plan, a canal: Panama"
    processed = preprocess(input)
    print(isPalindrom(processed))
