# Define two sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Union of E and N
union_result = E.union(N)
print(f"Union of E and N is {union_result}")

# Intersection of E and N
intersection_result = E.intersection(N)
print(f"Intersection of E and N is {intersection_result}")

# Difference of E and N (E - N)
difference_result = E.difference(N)
print(f"Difference of E and N is {difference_result}")

# Symmetric Difference of E and N
symmetric_difference_result = E.symmetric_difference(N)
print(f"Symmetric difference of E and N is {symmetric_difference_result}")
