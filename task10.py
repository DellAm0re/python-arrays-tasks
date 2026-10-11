
def sort_array_by_parity(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


print(sort_array_by_parity([3, 1, 2, 4]))
print(sort_array_by_parity([0]))
