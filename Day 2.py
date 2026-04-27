class Solution:
    def hasValidPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visited = set()

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return True

            visited.add((r, c))

            for dr, dc in dirs[grid[r][c]]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    for x, y in dirs[grid[nr][nc]]:
                        if nr + x == r and nc + y == c:
                            if dfs(nr, nc):
                                return True
            return False

        return dfs(0, 0)


# User Input
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))

grid = []

print("Enter grid row by row:")

for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

obj = Solution()

print("Valid Path Exists:", obj.hasValidPath(grid))