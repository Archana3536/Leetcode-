def rotateGrid(grid, k):
    m = len(grid)
    n = len(grid[0])

    layers = min(m, n) // 2

    for layer in range(layers):

        elements = []

        # top row
        for j in range(layer, n - layer):
            elements.append(grid[layer][j])

        # right column
        for i in range(layer + 1, m - layer - 1):
            elements.append(grid[i][n - layer - 1])

        # bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            elements.append(grid[m - layer - 1][j])

        # left column
        for i in range(m - layer - 2, layer, -1):
            elements.append(grid[i][layer])

        # rotate
        length = len(elements)
        k_rotate = k % length
        rotated = elements[k_rotate:] + elements[:k_rotate]

        idx = 0

        # top row
        for j in range(layer, n - layer):
            grid[layer][j] = rotated[idx]
            idx += 1

        # right column
        for i in range(layer + 1, m - layer - 1):
            grid[i][n - layer - 1] = rotated[idx]
            idx += 1

        # bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            grid[m - layer - 1][j] = rotated[idx]
            idx += 1

        # left column
        for i in range(m - layer - 2, layer, -1):
            grid[i][layer] = rotated[idx]
            idx += 1

    return grid


# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter matrix rows:")

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

k = int(input("Enter k value: "))

result = rotateGrid(grid, k)

print("Rotated Grid:")

for row in result:
    print(row)



# Enter number of rows: 4
# Enter number of columns: 4

# Enter matrix rows:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# Enter k value: 2
# [3, 4, 8, 12]
# [2, 11, 10, 16]
# [1, 7, 6, 15]
# [5, 9, 13, 14]