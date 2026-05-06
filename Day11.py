# Dynamic input version

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the box (use #, *, . separated by space):")

box = []
for i in range(rows):
    row = input().split()
    box.append(row)


def rotate_box(box):
    m = len(box)
    n = len(box[0])

    # Step 1: Gravity
    for i in range(m):
        empty = n - 1
        for j in range(n - 1, -1, -1):
            if box[i][j] == '*':
                empty = j - 1
            elif box[i][j] == '#':
                box[i][j] = '.'
                box[i][empty] = '#'
                empty -= 1

    # Step 2: Rotation
    res = [[None] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            res[j][m - 1 - i] = box[i][j]

    return res


result = rotate_box(box)

print("Rotated Box:")
for row in result:
    print(" ".join(row))

#  Enter number of rows: 2
# Enter number of columns: 4
# # . * .
# # # * .
# # .

# # #
# * *
# . .