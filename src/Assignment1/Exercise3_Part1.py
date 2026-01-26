import random

num_simulations = 10000

def simulate_same_day_birthday(num_people):
    matches = 0

    for _ in range(num_simulations):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]

        # Fetch matches by comparing length of list and set
        if len(birthdays) != len(set(birthdays)):
            matches += 1
    return matches / num_simulations


# Found 23 people to be the threshold for a >50% chance
#print(simulate_same_day_birthday(num_people=23)) # Uncomment to run the simulation Part 1

# Part 2

for N in range(10,50):
    probability = simulate_same_day_birthday(num_people=N)
    print(f"Number of People: {N}, Probability of Shared Birthday: {probability:.4f}")


