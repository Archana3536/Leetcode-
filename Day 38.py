n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = max(numbers)

print("Largest Number:", largest)

# Enter number of elements: 5
# Enter number: 12
# Enter number: 45
# Enter number: 78
# Enter number: 23
# Enter number: 56
# Largest Number: 78