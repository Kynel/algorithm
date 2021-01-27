def threeSum(nums):
    result = []
    nums.sort()

    length = len(nums)
    for i in range(length - 2):
        if nums[i] > 0 or (i > 0 and nums[i] == nums[i-1]):
            continue
        for j in range(i + 1, length - 1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j + 1, length):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i], nums[j], nums[k]))

    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
