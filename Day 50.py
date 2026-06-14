n = int(input("Enter even number of nodes: "))

arr = list(map(int, input("Enter node values: ").split()))

left = 0
right = n - 1
max_sum = 0

while left < right:
    twin_sum = arr[left] + arr[right]

    if twin_sum > max_sum:
        max_sum = twin_sum

    left += 1
    right -= 1

print("Maximum Twin Sum =", max_sum)

# Enter even number of nodes: 4
# Enter node values: 5 4 2 1
# Maximum Twin Sum = 6