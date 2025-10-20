num_triangles = int(input("How many triangles? "))
total_area = 0.0
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
total_area += area

for i in range(1, num_triangles + 1):
    print(f"\nTriangle {i}:")
    print(f"Area: {area}")
print(f"Total area of all triangles: {total_area}")