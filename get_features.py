from mods import Mods


def get_features(data):
    maxpp = max([float(x['pp']) for x in data])
    maxcombo = max([int(x['maxcombo']) for x in data])

    a = list(zip(
        [calculate_accuracy(d) for d in data],
        [float(d['pp']) / maxpp for d in data],
        [int(d['maxcombo']) / maxcombo for d in data],
        [has_mod(Mods.HardRock, d) for d in data],
        [has_mod(Mods.Hidden, d) for d in data],
        [has_mod(Mods.Hidden, d) and has_mod(Mods.HardRock, d) for d in data],
        [has_mod(Mods.Easy, d) for d in data],
        [has_mod(Mods.Flashlight, d) for d in data],
        [has_mod(Mods.Flashlight, d) and has_mod(Mods.HardRock, d) for d in data],
        [has_mod(Mods.Flashlight, d) and has_mod(Mods.Hidden, d) for d in data],
        [has_mod(Mods.Flashlight, d) and has_mod(Mods.HardRock, d) and has_mod(Mods.Hidden, d) for d in data],
        [has_mod(Mods.Flashlight, d) and has_mod(Mods.Easy, d) for d in data],
        [has_mod(Mods.Flashlight, d) and has_mod(Mods.Easy, d) and has_mod(Mods.Hidden, d) for d in data],
        [has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.HardRock, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Hidden, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.HardRock, d)) and (
            has_mod(Mods.Hidden, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Easy, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Easy, d)) and (
            has_mod(Mods.Hidden, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Flashlight, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Flashlight, d)) and (
            has_mod(Mods.HardRock, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Flashlight, d)) and (
            has_mod(Mods.Hidden, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Flashlight, d)) and (
            has_mod(Mods.HardRock, d)) and (has_mod(Mods.Hidden, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Flashlight, d)) and (
            has_mod(Mods.Easy, d)) for d in data],
        [(has_mod(Mods.DoubleTime, d) or has_mod(Mods.Nightcore, d)) and (has_mod(Mods.Flashlight, d)) and (
            has_mod(Mods.Easy, d)) and (has_mod(Mods.Hidden, d)) for d in data],
    ))
    return a


def calculate_accuracy(score):
    count50 = int(score['count50'])
    count100 = int(score['count100'])
    count300 = int(score['count300'])
    countmiss = int(score['countmiss'])
    acc = (count50 * 50 + count100 * 100 + count300 * 300) / (300 * (countmiss + count50 + count100 + count300))
    return round(acc, 2)


def has_mod(mod, score):
    score_mod = int(score['enabled_mods'])
    has = bool(mod & score_mod)
    return int(has)