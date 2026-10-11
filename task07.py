
def check_if_exist(arr):
    seen = set()

    for number in arr:
        if number * 2 in seen or (
            number % 2 == 0 and number // 2 in seen
        ):
            return True

        seen.add(number)

    return False


print(check_if_exist([10, 2, 5, 3]))
print(check_if_exist([3, 1, 7, 11]))
