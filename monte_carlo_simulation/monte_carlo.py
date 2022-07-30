import decimal
import statistics

from poker.five_card_draw import *


def multiple_trials(func):
    def wrapper(*args, **kwargs):
        results = []
        trials = kwargs.pop('trials', None)
        for i in range(trials):
            results.append(func(*args, **kwargs))
        mean = statistics.mean(results)
        return decimal.Decimal(mean)
    return wrapper
