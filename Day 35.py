def blockPlacementQueries(queries):
    obstacles = set()
    result = []

    for q in queries:

        if q[0] == 1:
            obstacles.add(q[1])

        else:
            x, sz = q[1], q[2]

            positions = [0]

            for obs in obstacles:
                if obs <= x:
                    positions.append(obs)

            positions.append(x)

            positions.sort()

            possible = False

            for i in range(1, len(positions)):
                if positions[i] - positions[i - 1] >= sz:
                    possible = True
                    break

            result.append(possible)

    return result


n = int(input("Enter number of queries: "))

queries = []

for i in range(n):

    query = list(map(int, input().split()))

    queries.append(query)

print(blockPlacementQueries(queries))

# Enter number of queries: 4
# 1 2
# 2 3 3
# 2 3 1
# 2 2 2
# [False, True, True]