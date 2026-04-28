class Solution:
    def minOperations(self, grid, x):
        nums = []

        for row in grid:
            for num in row:
                nums.append(num)

        rem = nums[0] % x
        for num in nums:
            if num % x != rem:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0
        for num in nums:
            operations += abs(num - median) // x

        return operations


# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []
print("Enter grid values row by row:")

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

x = int(input("Enter value of x: "))

obj = Solution()
print("Minimum Operations:", obj.minOperations(grid, x))

#Enter rows: 2
#Enter columns: 2
#Enter grid values:
#2 4
# 6 8
# Enter x value: 2
# Minimum Operations = 4
