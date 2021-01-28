def arrayPairSum1(nums):
    nums.sort()
    result = 0
    length = len(nums)
    for i in range(int(length/2)):
        result += min(nums[i*2], nums[i*2 + 1])

    return result


def arrayPairSum2(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


if __name__ == "__main__":
    nums = [1, 5, 3, 2, 7, 4]
    print(arrayPairSum1(nums))
    print(arrayPairSum2(nums))
