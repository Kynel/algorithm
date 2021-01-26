def rainTrap(heights):
    if not heights:
        return 0

    volume = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]

    while left < right:
        left_max, right_max = max(heights[left], left_max), max(
            heights[right], right_max)

        if left_max <= right_max:
            volume += left_max - heights[left]
            left += 1
        else:
            volume += right_max - heights[right]
            right -= 1

    return volume


if __name__ == "__main__":
    heights = [3, 1, 2, 3, 4, 1, 1, 2]
    print(rainTrap(heights))
