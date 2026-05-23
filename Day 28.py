# Dynamic Program

nums = list(map(int, input("Enter array elements: ").split()))

count = 0
n = len(nums)

for i in range(n):
    if nums[i] > nums[(i + 1) % n]:
        count += 1

if count <= 1:
    print("True")
else:
    print("False")

# 3 4 5 1 2
# True