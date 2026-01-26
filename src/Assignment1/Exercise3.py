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
