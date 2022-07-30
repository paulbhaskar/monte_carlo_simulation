import random

from monte_carlo_simulation.monte_carlo import multiple_trials


def flip_coin():
    return random.choice([0, 1])


def single_trial(n):
    arr = []
    for i in range(n):
        arr.append(flip_coin())
    return sum(arr)


print(multiple_trials(single_trial)(10, trials=1000))
