import numpy as np

transformation = np.array([[0.7,0.3],[0.3, 0.7]])

O_true = np.diag([0.9, 0.2])
O_false = np.diag([0.1, 0.8])

f = np.array([0.5, 0.5])

def forward(f_prev, observation):
    if observation:
        observation_matrix = O_true
    else:
        observation_matrix = O_false

    # Formula from expression 14.12 (p.492) in the textbook.
    f_pred = observation_matrix @ transformation.T @ f_prev

    # Normalize
    f_next = f_pred / np.sum(f_pred)
    return f_next



observations = [True, True ]

# Make sure to compute from 1, not 0.
for i, obs in enumerate(observations, start=1):
    f = forward(f, obs)
    print(f"f_1:{i} =  {f}")

print(f"\nP(R_2) = {observations}")
print("\nP(R_2 | e_1:2) =", f[0])
print("\n")



##################################


# Rain at day 5:

f2 = np.array([0.5, 0.5])

observations2 = [True, True, False, True, True]
print(f"\nP(R_5) = {observations2}")

# Make sure to compute from 1, not 0.
for i, obs in enumerate(observations2, start=1):
    f2 = forward(f2, obs)
    print(f"f_1:{i} =  {f2}")
print("\nP(R_5 | e_1:5) =", f2[0])       