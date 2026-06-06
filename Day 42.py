n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter elements: ").split()))

totalSum = sum(nums)
leftSum = 0

answer = []

for i in range(n):
    rightSum = totalSum - leftSum - nums[i]
    answer.append(abs(leftSum - rightSum))
    leftSum += nums[i]

print("Answer:", answer)

# Enter number of elements: 4
# Enter elements: 10 4 8 3
# Answer: [15, 1, 11, 22]