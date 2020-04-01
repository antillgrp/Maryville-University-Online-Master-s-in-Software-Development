from random import randint


def minMaxRecursive(numbers):
    return numbers[0] if len(numbers) == 1 else min(
        numbers[0],
        minMaxRecursive(numbers[1 if 1 < len(numbers) else 0:])[0]
    ), numbers[0] if len(numbers) == 1 else max(
        numbers[0],
        minMaxRecursive(numbers[1 if 1 < len(numbers) else 0:])[1]
    )


def reverseRecursive(numbers):
    return numbers[:len(numbers)] if len(numbers) < 1 else reverseRecursive(numbers[1:]) + numbers[:1]


nums = [randint(-10, 50) for i in range(20)]
print("Original Array: ", nums)
print("Min: {}, Max: {}".format(*minMaxRecursive(nums)))
print("Reverse: ", reverseRecursive(nums))
