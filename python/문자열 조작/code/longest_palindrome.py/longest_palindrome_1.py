def isPalindrome(input):
    if (input[::-1] == input):
        return True
    return False


def longestPalindrome(input):
    length = len(input)
    step = length
    answer = ""
    breakpoint = False

    while step > 2:
        for i in range(length-step+1):
            if(isPalindrome(input[i:i+step])):
                answer = input[i:i+step]
                breakpoint = True
                break
        if(breakpoint):
            break
        step -= 1

    return answer


if __name__ == "__main__":
    input = "babad"
    print(longestPalindrome(input))
