def maxPathScore(grid, k):
    m = len(grid)
    n = len(grid[0])

    # dp[r][c] = dictionary {cost: max_score}
    dp = [[{} for _ in range(n)] for _ in range(m)]

    # Initialize
    dp[0][0][0] = 0

    for i in range(m):
        for j in range(n):
            for cost, score in dp[i][j].items():

                # Move Right
                if j + 1 < n:
                    val = grid[i][j+1]
                    new_cost = cost + (1 if val > 0 else 0)
                    new_score = score + val

                    if new_cost <= k:
                        dp[i][j+1][new_cost] = max(
                            dp[i][j+1].get(new_cost, 0),
                            new_score
                        )

                # Move Down
                if i + 1 < m:
                    val = grid[i+1][j]
                    new_cost = cost + (1 if val > 0 else 0)
                    new_score = score + val

                    if new_cost <= k:
                        dp[i+1][j][new_cost] = max(
                            dp[i+1][j].get(new_cost, 0),
                            new_score
                        )

    # Get maximum score at destination
    if not dp[m-1][n-1]:
        return -1

    return max(dp[m-1][n-1].values())
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))

print("Enter grid values:")
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

k = int(input("Enter max cost (k): "))
result = maxPathScore(grid, k)
print("Maximum Score:", result)

# Input/output
# Enter rows: 2
# Enter columns: 2
# Enter grid values:
# 0 1
# 2 0
# Enter max cost (k): 1
# Maximum Score: 2