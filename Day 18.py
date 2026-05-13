class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        ans = float('inf')

        for target in range(2, 2 * limit + 1):
            moves = 0

            for i in range(n // 2):
                a = nums[i]
                b = nums[n - 1 - i]

                if a + b == target:
                    continue
                elif 1 <= target - a <= limit or 1 <= target - b <= limit:
                    moves += 1
                else:
                    moves += 2

            ans = min(ans, moves)

        return ans


nums = list(map(int, input("Enter array elements: ").split()))
limit = int(input("Enter limit value: "))

obj = Solution()

print("Minimum Moves:", obj.minMoves(nums, limit))

# Enter array elements: 1 2 4 3
# Enter limit value: 4
# Minimum Moves: 1