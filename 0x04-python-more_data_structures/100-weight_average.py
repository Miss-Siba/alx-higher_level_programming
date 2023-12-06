#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or not all(
            isinstance(item, tuple) and len(item) == 2
            for item in my_list
    ):
        return (0)

    total_weighted_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    if total_weight == 0:
        return (0)

    return total_weighted_score / total_weight
