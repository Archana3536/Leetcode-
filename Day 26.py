class Solution:
    def longestCommonPrefix(self, arr1, arr2):

        prefixes = set()

        for num in arr1:
            s = str(num)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        answer = 0

        for num in arr2:
            s = str(num)

            for i in range(1, len(s) + 1):

                if s[:i] in prefixes:
                    answer = max(answer, i)

        return answer


arr1 = list(map(int, input("Enter first array elements: ").split()))
arr2 = list(map(int, input("Enter second array elements: ").split()))

obj = Solution()

print("Longest Common Prefix Length:",
      obj.longestCommonPrefix(arr1, arr2))

# Enter first array elements: 1 10 100
# Enter second array elements: 1000
# Longest Common Prefix Length: 3