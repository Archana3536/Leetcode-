n = int(input("Enter number of candies: "))

cost = list(map(int, input("Enter candy costs: ").split()))

cost.sort(reverse=True)

total = 0

for i in range(len(cost)):
    if i % 3 != 2:
        total += cost[i]

print("Minimum Cost =", total)

# Enter number of candies: 6
# Enter candy costs: 6 5 7 9 2 2
# Minimum Cost = 23