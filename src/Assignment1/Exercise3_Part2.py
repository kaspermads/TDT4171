import random
import numpy as np



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



