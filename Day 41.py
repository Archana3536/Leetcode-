def waviness(num):
    s = str(num)
    count = 0

    for i in range(1, len(s) - 1):
        left = int(s[i - 1])
        mid = int(s[i])
        right = int(s[i + 1])

        if (mid > left and mid > right) or \
           (mid < left and mid < right):
            count += 1

    return count


num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))

total = 0

for n in range(num1, num2 + 1):
    total += waviness(n)

print("Total Waviness =", total)



# Enter starting number: 120
# Enter ending number: 130
# Total Waviness = 3