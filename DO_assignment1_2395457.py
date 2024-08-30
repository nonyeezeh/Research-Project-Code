# Question 1
# Value and weight pairs
items = [(2, 7), (6, 3), (8, 3), (7, 5), (3, 4), (4, 7), (6, 5), (5, 4), (10, 15), (9, 10),
         (8, 17), (11, 3), (12, 6), (15, 11), (6, 6), (8, 14), (13, 4), (14, 8), (15, 9), 
         (16, 10), (13, 14), (14, 17), (15, 9), (26, 24), (13, 11), (9, 17), (25, 12), (26, 14)]

# Knapsack Capacity
capacity = 30

# Sort items based on the value-to-weight ratio in descending order for efficiency function
items.sort(key=lambda x: x[0] / x[1], reverse=True)

total_weight = 0
total_value = 0
selected_items = []

# Select items until the knapsack is full
for value, weight in items:
    if total_weight + weight <= capacity:
        selected_items.append((value, weight))
        total_weight += weight
        total_value += value

# Display the selected items
print("Question 1")
print("--------------------------------")
print("Selected items:", selected_items)
print("Total weight:", total_weight)
print("Total value:", total_value)

#--------------------------------------------------------------------------

#Question 2
import numpy as np
from itertools import combinations

# Distance matrix
M = np.array([
    [0, 1.5, 3, 13, 3.5, 4.5, 1.5],
    [1.5, 0, 1.5, 1.3, 13, 13, 2.3],
    [3, 1.5, 0, 1.5, 3, 13, 3],
    [13, 1.3, 1.5, 0, 1.5, 13, 20],
    [3.5, 13, 3, 1.5, 0, 1.5, 3.3],
    [4.5, 13, 13, 13, 1.5, 0, 1.5],
    [1.5, 2.3, 3, 20, 3.3, 1.5, 0]
])

# Starting tour
tour = [1, 3, 5, 7, 4, 6, 2, 1]

# Initial distance calculation
total_distance = 0.0
for i in range(len(tour) - 1):
    total_distance += float(M[tour[i] - 1, tour[i + 1] - 1])

best_tour = tour[:]
best_distance = round(total_distance, 2)
improvements = [(best_tour, best_distance)]
improvement_found = True

# Perform 2-opt
while improvement_found:
    improvement_found = False
    for i, j in combinations(range(1, len(tour) - 2), 2):
        new_tour = best_tour[:i] + best_tour[i:j + 1][::-1] + best_tour[j + 1:]
        new_distance = 0.0
        for k in range(len(new_tour) - 1):
            new_distance += float(M[new_tour[k] - 1, new_tour[k + 1] - 1])

        new_distance = round(new_distance, 2) 

        if new_distance < best_distance:
            best_tour = new_tour[:]
            best_distance = new_distance
            improvements.append((best_tour, best_distance))
            improvement_found = True

# Display Final outputs
print("\nQuestion 2")
print("--------------------------------")
print("Improving Solutions:")
for solution in improvements:
    print(f"Tour: {solution[0]}, Distance: {solution[1]}")
print("Final Tour:", best_tour)
print("Final Distance:", best_distance)

