
def replace_elements(arr):
    largest_right = -1

    for i in range(len(arr) - 1, -1, -1):
        original = arr[i]

        arr[i] = largest_right

        largest_right = max(largest_right, original)

    return arr


print(replace_elements([17, 18, 5, 4, 6, 1]))
print(replace_elements([400]))
