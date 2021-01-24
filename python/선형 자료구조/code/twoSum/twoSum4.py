def twoSum(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


if __name__ == "__main__":
    nums = [2, 2, 11, 15]
    target = 4

    print(twoSum(nums, target))
