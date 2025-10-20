lower = int(input("What is the lower bound: "))
higher = int(input("What is the higher bound: "))
total = 0

for i in range(lower, higher + 1):
    total += i

print(f"The sum of numbers from {lower} to {higher} is {total}")