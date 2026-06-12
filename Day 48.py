from typing import List
from collections import deque
import math

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        MOD = 1000000007
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = math.ceil(math.log2(n)) + 1

        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()

            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    depth[nxt] = depth[node] + 1
                    parent[0][nxt] = node
                    q.append(nxt)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for i in range(LOG):
                if diff & (1 << i):
                    u = parent[i][u]

            if u == v:
                return u

            for i in range(LOG - 1, -1, -1):
                if parent[i][u] != parent[i][v]:
                    u = parent[i][u]
                    v = parent[i][v]

            return parent[0][u]

        ans = []

        for u, v in queries:

            ancestor = lca(u, v)

            length = depth[u] + depth[v] - 2 * depth[ancestor]

            if length == 0:
                ans.append(0)
            else:
                ans.append(pow(2, length - 1, MOD))

        return ans
    
# edges = [[1,2],[1,3],[3,4],[3,5]]

# queries = [[1,4],[3,4],[2,5]]
# [2,1,4]