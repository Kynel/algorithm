def threeSum(nums):
    result = []
    nums.sort()

    length = len(nums)
    for i in range(length - 2):
        if nums[i] > 0 or (i > 0 and nums[i] == nums[i - 1]):
            continue
        left, right = i + 1, length - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                print(result)

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


if __name__ == "__main__":
    nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    print(threeSum(nums))
