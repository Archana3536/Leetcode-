class Solution:
    def canReach(self, s, minJump, maxJump):

        n = len(s)

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):

            if i >= minJump:
                reachable += dp[i - minJump]

            if i > maxJump:
                reachable -= dp[i - maxJump - 1]

            if reachable > 0 and s[i] == '0':
                dp[i] = True

        return dp[-1]


s = input("Enter binary string: ")
minJump = int(input("Enter minJump: "))
maxJump = int(input("Enter maxJump: "))

obj = Solution()

print(obj.canReach(s, minJump, maxJump))

# 011010
# 2
# 3
# True