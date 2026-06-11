from typing import List
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 1000000007

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([1])
        visited = [False] * (n + 1)

        visited[1] = True

        depth = -1

        while q:
            depth += 1

            for _ in range(len(q)):
                node = q.popleft()

                for nxt in graph[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)

        return pow(2, depth - 1, MOD)
    

    edges = [[1,2]]
    1 --- 2