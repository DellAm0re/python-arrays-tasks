
def find_max_consecutive_ones(nums):
    maximum = 0
    current = 0

    for number in nums:
        if number == 1:
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0

    return maximum


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))
