class Solution:
    def isGood(self, nums):
        nums.sort()

        n = nums[-1]

        expected = list(range(1, n)) + [n, n]

        return nums == expected


nums = list(map(int, input("Enter array elements: ").split()))

obj = Solution()

print("Is Array Good?", obj.isGood(nums))


# Enter array elements: 1 3 3 2
# Is Array Good? True