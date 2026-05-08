from collections import deque, defaultdict

def isPrime(x):
    if x < 2:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


def minJumps(nums):

    n = len(nums)

    divisible = defaultdict(list)

    for i in range(n):
        for j in range(n):
            if i != j and nums[j] % nums[i] == 0:
                divisible[i].append(j)

    queue = deque([(0, 0)])
    visited = set([0])

    while queue:

        index, steps = queue.popleft()

        if index == n - 1:
            return steps

        # Left move
        if index - 1 >= 0 and (index - 1) not in visited:
            visited.add(index - 1)
            queue.append((index - 1, steps + 1))

        # Right move
        if index + 1 < n and (index + 1) not in visited:
            visited.add(index + 1)
            queue.append((index + 1, steps + 1))

        # Prime teleportation
        if isPrime(nums[index]):

            for next_index in divisible[index]:

                if next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

    return -1


nums = list(map(int, input("Enter array elements: ").split()))

result = minJumps(nums)

print("Minimum jumps:", result)