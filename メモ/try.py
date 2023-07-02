def cmp(A):
    cmpB = sorted(set(A))
    cmpD = { v: i for i, v in enumerate(cmpB)}
    return list(map(lambda v: cmpD[v], A))