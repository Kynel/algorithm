def arrayPairSum(nums):
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print(arrayPairSum(nums))
