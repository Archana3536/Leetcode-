from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        for i, value in enumerate(arr):
            graph[value].append(i)

        queue = deque([(0, 0)])
        visited = set([0])

        while queue:
            index, steps = queue.popleft()

            if index == n - 1:
                return steps

            neighbors = graph[arr[index]] + [index - 1, index + 1]

            for next_index in neighbors:
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

            graph[arr[index]].clear()


arr = list(map(int, input("Enter array elements: ").split()))

obj = Solution()
print("Minimum Jumps:", obj.minJumps(arr))

# Enter array elements: 100 -23 -23 404 100 23 23 23 3 404
# Minimum Jumps: 3