n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter array elements: ").split()))

k = int(input("Enter value of k: "))

max_val = max(nums) - min(nums)

result = k * max_val

print("Maximum Total Subarray Value:", result)

# Enter number of elements: 5
# Enter array elements: 4 2 5 1 1
# Enter value of k: 3
# Maximum Total Subarray Value: 12