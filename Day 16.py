def separateDigits(nums):
    result = []

    for num in nums:
        digits = str(num)

        for digit in digits:
            result.append(int(digit))

    return result


# User Input
nums = list(map(int, input("Enter array elements: ").split()))

result = separateDigits(nums)

print("Separated Digits:", result)

# Enter array elements: 13 25 83 77
# Separated Digits: [1, 3, 2, 5, 8, 3, 7, 7]