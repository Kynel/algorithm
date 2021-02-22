def lengthOfLongestSubstring(self, s):
    used = {}
    max_length = start = 0

    for i, char in enumerate(s):
        if (char in used) and (start <= used[char]):  # 1
            start = used[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[char] = i

    return max_length
