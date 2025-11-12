import random

module_name = "random"


def chance(probability):
    if probability < 0 or probability > 1:
        raise ValueError("Probability must be between 0 and 1")
    if random.random() < probability:
        return True
    else:
        return False
