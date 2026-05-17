class Solution:
    def canReach(self, arr, start):
        visited = set()

        def dfs(i):
            if i < 0 or i >= len(arr) or i in visited:
                return False

            if arr[i] == 0:
                return True

            visited.add(i)

            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)


arr = list(map(int, input("Enter array elements: ").split()))
start = int(input("Enter start index: "))

obj = Solution()
print(obj.canReach(arr, start))

# Enter array elements: 4 2 3 0 3 1 2
# Enter start index: 5
# True