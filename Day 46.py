n = int(input("Enter size of array: "))

nums = list(map(int, input("Enter array elements: ").split()))

k = int(input("Enter k value: "))

subarray_values = []

for i in range(n):
    mx = mn = nums[i]

    for j in range(i, n):
        mx = max(mx, nums[j])
        mn = min(mn, nums[j])

        subarray_values.append(mx - mn)

subarray_values.sort(reverse=True)

answer = sum(subarray_values[:k])

print("Maximum Total Subarray Value =", answer)

# Enter size of array: 4
# Enter array elements: 4 2 5 1
# Enter k value: 3
# Maximum Total Subarray Value = 12