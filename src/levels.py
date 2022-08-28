
from random import shuffle

LEVEL1 = [
    1, 1, 1, 1, 1, 1
]
LEVEL1_FINAL_WAVE = [
    1, 1, 1, 1, 1, 1
]
LEVEL1_TRIGGER = {
    "first": None,
    "second": None,
    "third": None,
    "final": len(LEVEL1)
}
LEVEL1_LANE = []

# LEVEL MODIFIER || DON'T CHANGE


def level_maker_chain(*type_and_num: list, random_it=False):
    # Chain Method
    result = list()
    for length in type_and_num:
        result += [length[0] for _ in range(length[1])]
    if random_it:
        shuffle(result)
    return result


def level_maker_iterator(type_and_num: list, random_it=False):
    result = list()
    for length in range(len(type_and_num)):
        result += [type_and_num[length][0]
                   for _ in range(type_and_num[length][1])]
    if random_it:
        shuffle(result)
    return result


ALL_ENEMY_TYPE = {
    1: "ordinary",
}

ALL_LEVEL = [
    {
        # LEVEL 1
        "string": "LEVEL1",
        "level": level_maker_chain([1, 7]),
        "first_wave": None,
        "second_wave": None,
        "third_wave": None,
        "final_wave": level_maker_chain([1, 8]),
        "trigger": LEVEL1_TRIGGER,
        "lane": []
    }
]

LEVEL_SCRIPT = [
    80, 100, 70,
]

LEVEL_SCRIPT_CHOICE = {
    "0": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "1": [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],  # Num of zombie 3
    "2": [1, 1, 2, 2, 2, 2, 2, 2, 3, 3],  # Num of zombie 6
    "3": [2, 2, 2, 2, 2, 2, 3, 3, 3, 3],  # Num of zombie 15
    "4": [2, 2, 2, 2, 3, 3, 3, 3, 3, 4],  # Num of zombie 25
    "5": [2, 3, 3, 3, 3, 3, 4, 4, 4, 4],  # Num of zombie 40
    "6": [3, 3, 3, 4, 4, 4, 4, 5, 5, 5],  # Num of zombie 60
}
