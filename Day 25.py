class Solution:
    def findThePrefixCommonArray(self, A, B):
        setA = set()
        setB = set()
        result = []

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])

            common = len(setA.intersection(setB))
            result.append(common)

        return result


A = list(map(int, input("Enter elements of array A: ").split()))
B = list(map(int, input("Enter elements of array B: ").split()))

obj = Solution()
print("Prefix Common Array:", obj.findThePrefixCommonArray(A, B))

# Enter elements of array A: 1 3 2 4
# Enter elements of array B: 3 1 2 4
# Prefix Common Array: [0, 2, 3, 4]