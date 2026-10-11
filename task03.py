
def sorted_squares(nums):
    left = 0
    right = len(nums) - 1

    result = [0] * len(nums)
    position = len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[position] = nums[left] * nums[left]
            left += 1
        else:
            result[position] = nums[right] * nums[right]
            right -= 1

        position -= 1

    return result


print(sorted_squares([-4, -1, 0, 3, 10]))
print(sorted_squares([-7, -3, 2, 3, 11]))
