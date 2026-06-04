def waviness(num):
    s = str(num)
    count = 0

    for i in range(1, len(s) - 1):
        if (s[i] > s[i - 1] and s[i] > s[i + 1]) or \
           (s[i] < s[i - 1] and s[i] < s[i + 1]):
            count += 1

    return count


num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))

total = 0

for n in range(num1, num2 + 1):
    total += waviness(n)

print("Total Waviness =", total)

# Enter starting number: 198
# Enter ending number: 202
# Total Waviness = 3