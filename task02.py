
def find_numbers(nums):
    count = 0

    for number in nums:
        if len(str(number)) % 2 == 0:
            count += 1

    return count


print(find_numbers([12, 345, 2, 6, 7896]))
print(find_numbers([555, 901, 482, 1771]))
