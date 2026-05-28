class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        result = []

        for query in wordsQuery:
            best_index = 0
            best_suffix = ""

            for i in range(len(wordsContainer)):
                word = wordsContainer[i]

                suffix = ""
                a = len(word) - 1
                b = len(query) - 1

                while a >= 0 and b >= 0 and word[a] == query[b]:
                    suffix = word[a] + suffix
                    a -= 1
                    b -= 1

                if len(suffix) > len(best_suffix):
                    best_suffix = suffix
                    best_index = i

                elif len(suffix) == len(best_suffix):
                    if len(word) < len(wordsContainer[best_index]):
                        best_index = i

            result.append(best_index)

        return result


# Dynamic Input
n = int(input("Enter number of words in container: "))

wordsContainer = []

for i in range(n):
    word = input(f"Enter word {i+1}: ")
    wordsContainer.append(word)

m = int(input("Enter number of query words: "))

wordsQuery = []

for i in range(m):
    query = input(f"Enter query word {i+1}: ")
    wordsQuery.append(query)

obj = Solution()

print("Result:", obj.stringIndices(wordsContainer, wordsQuery))


# Enter number of words in container: 3
# Enter word 1: abcd
# Enter word 2: bcd
# Enter word 3: xbcd

# Enter number of query words: 3
# Enter query word 1: cd
# Enter query word 2: bcd
# Enter query word 3: xyz

# Result: [1, 1, 1]