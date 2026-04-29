class Solution:
    def titleToNumber(self, columnTitle):
        result = 0

        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)

        return result


# User Input
columnTitle = input("Enter Excel Column Title: ")

obj = Solution()
print("Column Number:", obj.titleToNumber(columnTitle))

# User input/outpu:
# AB
# Column Number: 28