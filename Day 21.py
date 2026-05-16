class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]


nums = list(map(int, input("Enter array elements: ").split()))

obj = Solution()
print("Minimum Element:", obj.findMin(nums))

# Enter array elements: 2 2 2 0 1
# Minimum Element: 0