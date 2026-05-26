class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = set()
        uppercase = set()

        for ch in word:
            if ch.islower():
                lowercase.add(ch)
            else:
                uppercase.add(ch.lower())

        count = 0

        for ch in lowercase:
            if ch in uppercase:
                count += 1

        return count


word = input("Enter the word: ")

obj = Solution()

print("Special characters count:", obj.numberOfSpecialChars(word))

# Enter the word: aaAbcBC
# Special characters count: 3