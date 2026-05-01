def maxRotateFunction(nums):
    n = len(nums)
    
    total_sum = sum(nums)
    
    # Calculate F(0)
    F = 0
    for i in range(n):
        F += i * nums[i]
    
    max_val = F
    
    # Compute next rotations using formula
    for k in range(1, n):
        F = F + total_sum - n * nums[n - k]
        max_val = max(max_val, F)
    
    return max_val

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements: ").split()))
result = maxRotateFunction(nums)
print("Maximum Rotate Function Value:", result)

# input/output
# Enter number of elements: 4
# Enter elements: 4 3 2 6
# Maximum Rotate Function Value: 26