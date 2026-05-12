class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:
            if current < minimum:
                energy += minimum - current
                current = minimum

            current -= actual

        return energy


n = int(input("Enter number of tasks: "))

tasks = []

for i in range(n):
    actual = int(input(f"Enter actual energy for task {i+1}: "))
    minimum = int(input(f"Enter minimum energy for task {i+1}: "))
    tasks.append([actual, minimum])

obj = Solution()

print("Minimum Initial Energy:", obj.minimumEffort(tasks))

# Enter number of tasks: 3
# Enter actual energy for task 1: 1
# Enter minimum energy for task 1: 2
# Enter actual energy for task 2: 2
# Enter minimum energy for task 2: 4
# Enter actual energy for task 3: 4
# Enter minimum energy for task 3: 8
    
# Minimum Initial Energy: 8