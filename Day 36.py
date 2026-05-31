mass = int(input("Enter planet mass: "))

n = int(input("Enter number of asteroids: "))

asteroids = list(map(int, input("Enter asteroid masses: ").split()))

asteroids.sort()

possible = True

for asteroid in asteroids:
    if mass < asteroid:
        possible = False
        break
    mass += asteroid

print("Can destroy all asteroids:", possible)


# Enter planet mass: 10
# Enter number of asteroids: 5
# Enter asteroid masses: 3 9 19 5 21
# Can destroy all asteroids: True