def nearest_value_m(values: set, one: int) -> int:
    #16 DEC 2021
    nv = dict()
    for i in values:
        nv[i] = abs(one - i)
    nv = sorted(nv.items(), key=lambda item: item[1])
    min_dist = nv[0][0]
    if nv[0][1] == nv[1][1] and nv[1][0] < nv[0][0]:
        min_dist = nv[1][0]
    return min_dist

def nearest_value_b(values: set, one: int) -> int:
    # BEST SOLUTION
    return sorted(values, key=lambda k: (abs(k - one), k))[0]

# **********************