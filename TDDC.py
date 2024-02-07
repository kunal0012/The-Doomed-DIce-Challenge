# Solved By Kunal Bhardwaj


# [PART A]
total_combinations = 6 * 6
 # Total number of combinations is the product of the number of faces on both dice
print("Total Combinations:", total_combinations)




# creating a 6x6 matrix to represent all possible combinations of rolling both dice together
distribution = [[i + j for j in range(1, 7)] for i in range(1, 7)]
print("\nDistribution:")
for row in distribution:
    print(row)




# calculating the probability of each possible sum occurring.
probabilities = [0] * 11
for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i + j - 2] += 1

probabilities = [prob / total_combinations for prob in probabilities]
print("\nProbabilities:")
for i, prob in enumerate(probabilities):
    print("\nP(Sum =", i + 2, ") =", prob)

print("OUTPUT For Part A!")

# [PART B]
    
def undoom_dice(die_A, die_B):
    # Calculate the current probabilities of obtaining each sum with the original dice
    current_probs = [0] * 11
    for i in range(1, 7):
        for j in range(1, 7):
            current_probs[i + j - 2] += 1

    # Calculate the target probabilities for each sum
    total_combinations = 6 * 6
    target_probs = [prob / total_combinations for prob in current_probs]

    # Initialize the new dice with empty lists
    new_die_A = []
    new_die_B = []

    # Calculate the maximum number of spots allowed on Die A
    max_spots_A = min(4, max(die_A))

    # Attach spots to Die A while maintaining the probabilities
    for i in range(1, 7):
        for j in range(1, 7):
            # Calculate the sum of the current combination
            total = i + j
            # If the sum's probability matches the target, add spots to Die A
            if target_probs[total - 2] != 0:
                if i <= max_spots_A:
                    new_die_A.append(i)
                    new_die_B.append(j)
                    break

    # Fill the rest of Die A with 4s to satisfy the condition
    while len(new_die_A) < 6:
        new_die_A.append(4)
    
    # Die B remains unchanged
    new_die_B.extend(die_B[len(new_die_B):])

    return new_die_A, new_die_B

# Input dice
die_A = [1, 2, 3, 4, 5, 6]
die_B = [1, 2, 3, 4, 5, 6]

# Perform the transformation
new_die_A, new_die_B = undoom_dice(die_A, die_B)

# Output the new dice
print("\nNew Die A:", new_die_A)
print("\nNew Die B:", new_die_B)

print("OUTPUT For Part B!")
