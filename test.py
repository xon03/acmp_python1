# Possible ab values
options = [96, 102, 106, 108]

for ab in options:
    # Try integer values of b from 1 to 500 (you can increase this if needed)
    for b in range(1, 2000):
        a = ab / b
        if 4 * a - 7 * b + 28 * a * b == 2020:
            print(f"ab = {ab}, a = {a}, b = {b}")
            break
