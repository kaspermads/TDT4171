import random

import numpy as np

payout_scheme = [20, 15, 5, 3, 2, 1, 0]
payout_probabilities = [1/64, 1/64, 1/64, 1/64, 3/64, 12/64, 45/64]


initial_coins = 10
def simulate_game():
    coins = initial_coins
    plays = 0

    while coins > 0:
        coins -= 1
        plays += 1

        payout = random.choices(payout_scheme, payout_probabilities)[0]
        coins += payout
        plays += 1

    return plays

N = 100000

results = [simulate_game() for _ in range(N)]

mean_plays = np.mean(results)
median_plays = np.median(results)

print(f"After simulating {N} games:")
print(f"Mean number of plays: {mean_plays}")
print(f"Median number of plays: {median_plays}")

####################################################################

#Part 1

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


####################################################################
#Part 2

def simulate_group_birthday():
    count = 0
    group  = set()

    while len(group) < 365:
        random_birthday = random.randint(1, 365)
        group.add(random_birthday)
        count += 1

    return count


num_simulations  = 10000

results = [simulate_group_birthday() for _ in range(num_simulations)]

print(f"After simulating {num_simulations} groups:")
print(np.mean(results), np.median(results))




