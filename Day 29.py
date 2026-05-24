from functools import lru_cache

arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter jump distance d: "))

n = len(arr)

@lru_cache(None)
def dfs(i):
    ans = 1

    # Right side
    for j in range(i + 1, min(n, i + d + 1)):
        if arr[j] >= arr[i]:
            break
        ans = max(ans, 1 + dfs(j))

    # Left side
    for j in range(i - 1, max(-1, i - d - 1), -1):
        if arr[j] >= arr[i]:
            break
        ans = max(ans, 1 + dfs(j))

    return ans

result = max(dfs(i) for i in range(n))

print("Maximum indices visited:", result)

# 6 4 14 6 8 13 9 7 10 6 12
# 2
# Maximum indices visited: 4