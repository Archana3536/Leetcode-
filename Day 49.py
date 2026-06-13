weights = list(map(int, input("Enter 26 weights: ").split()))

n = int(input("Enter number of words: "))

words = []

for i in range(n):
    words.append(input("Enter word: "))

result = ""

for word in words:

    total = 0

    for ch in word:
        total += weights[ord(ch) - ord('a')]

    rem = total % 26

    mapped = chr(ord('z') - rem)

    result += mapped

print("Output:", result)

# Enter 26 weights:
# 5 3 12 14 1 2 3 2 10 6 6 9 7 8 7 10 8 9 6 9 9 8 3 7 7 2

# Enter number of words:
# 3

# Enter word:
# abcd

# Enter word:
# def

# Enter word:
# xyz
# Output: rij