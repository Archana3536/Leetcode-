# Happy Number - User Input Program

def isHappy(n):
    seen = set()

    while n != 1:

        # If number repeats, cycle found
        if n in seen:
            return False

        seen.add(n)

        total = 0

        # Find sum of square of digits
        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10

        n = total

    return True


# Dynamic Input
n = int(input("Enter a number: "))

if isHappy(n):
    print("Happy Number")
else:
    print("Not a Happy Number")

# Enter a number: 19
# Happy Number