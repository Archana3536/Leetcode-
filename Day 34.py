class Solution:

    def digitSum(self, num):

        total = 0

        while num > 0:
            total += num % 10
            num //= 10

        return total

    def minElement(self, nums):

        minimum = float('inf')

        for num in nums:

            s = self.digitSum(num)

            minimum = min(minimum, s)

        return minimum


nums = list(map(int, input("Enter array elements: ").split()))

obj = Solution()

print("Minimum Element:", obj.minElement(nums))


# Enter array elements: 10 12 13 14
# Minimum Element: 1