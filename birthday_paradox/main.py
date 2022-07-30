import random

from monte_carlo_simulation.monte_carlo import multiple_trials


def generate_random_birthday():
    return random.randint(0, 364)


def single_trial(n):
    arr = []
    for person in range(n):
        arr.append(generate_random_birthday())
    if (len(set(arr)) != len(arr)):
        return True
    else:
        return False


print(multiple_trials(single_trial)(30, trials=100000))
