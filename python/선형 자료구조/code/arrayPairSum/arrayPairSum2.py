def arrayPairSum(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5]
    print(arrayPairSum(nums))
