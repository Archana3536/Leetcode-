class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


nums = list(map(int, input("Enter rotated sorted array elements: ").split()))

obj = Solution()

print("Minimum element:", obj.findMin(nums))

# Enter rotated sorted array elements: 3 4 5 1 2
# Minimum element: 1