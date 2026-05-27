class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in word and ch.upper() in word:
                if word.rfind(ch) < word.find(ch.upper()):
                    result += 1

        return result


# Dynamic Input
word = input("Enter the string: ")

obj = Solution()

print("Special Characters Count:", obj.numberOfSpecialChars(word))


# Enter the string: aaAbcBC
# Special Characters Count: 3