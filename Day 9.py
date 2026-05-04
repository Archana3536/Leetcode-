# Rotate Image using user input

n = int(input("Enter size of matrix: "))

matrix = []
print("Enter matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 1: Transpose matrix
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Step 2: Reverse each row
for i in range(n):
    left = 0
    right = n - 1
    while left < right:
        matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
        left += 1
        right -= 1

print("Rotated Matrix:")

for row in matrix:
    print(row)




#     input /output:
#     Enter size of matrix: 3
# Enter matrix row by row:
# 1 2 3
# 4 5 6
# 7 8 9

# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]