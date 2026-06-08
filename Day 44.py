n = int(input("Enter size of array: "))

nums = list(map(int, input("Enter array elements: ").split()))

pivot = int(input("Enter pivot element: "))

less = []
equal = []
greater = []

for num in nums:
    if num < pivot:
        less.append(num)
    elif num == pivot:
        equal.append(num)
    else:
        greater.append(num)

result = less + equal + greater

print("Partitioned Array:", result)


# Enter size of array: 7
# Enter array elements: 9 12 5 10 14 3 10
# Enter pivot element: 10
# Partitioned Array: [9, 5, 3, 10, 10, 12, 14]