def numJewelsInStones1(self, jewels, stones):
    freqs = collections.defaultdict(int)
    result = 0

    for char in stones:
        freqs[char] += 1

    for char in jewels:  # !
        result += freqs[char]

    return result


def numJewelsInStones2(self, jewels, stones):
    freqs = collections.Counter(stones)  # 빈도 수 계산
    result = 0

    for char in jewels:
        result += freqs[char]

    return result


def numJewelsInStones3(self, jewels, stones):
    return sum(s in stones for s in jewels)
