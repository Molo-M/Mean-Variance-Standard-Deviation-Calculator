import numpy as np


def calculate(vals):

    # error handling
    if len(vals) != 9:
        raise ValueError('List must contain nine numbers.')

    ar = np.array(vals)
    matr = ar.reshape(3, 3)

    # finding mean
    col = matr.mean(axis=0)
    col = col.tolist()
    row = matr.mean(axis=1)
    row = row.tolist()
    flat = ar.mean()
    n_mean = [col, row, flat]

    # finding variance
    col = matr.var(axis=0)
    col = col.tolist()
    row = matr.var(axis=1)
    row = row.tolist()
    flat = ar.var()
    var = [col, row, flat]

    # standard deviation
    col = matr.std(axis=0)
    col = col.tolist()
    row = matr.std(axis=1)
    row = row.tolist()
    flat = ar.std()
    std_dv = [col, row, flat]

    # finding max
    col = matr.max(axis=0)
    col = col.tolist()
    row = matr.max(axis=1)
    row = row.tolist()
    flat = ar.max()
    max_v = [col, row, flat]

    # finding min
    col = matr.min(axis=0)
    col = col.tolist()
    row = matr.min(axis=1)
    row = row.tolist()
    flat = ar.min()
    min_v = [col, row, flat]

    # finding sum
    col = matr.sum(axis=0)
    col = col.tolist()
    row = matr.sum(axis=1)
    row = row.tolist()
    flat = ar.sum()
    sum_v = [col, row, flat]

    # Fill dictionary
    calculations = dict()
    calculations['mean'] = n_mean
    calculations['variance'] = var
    calculations['standard deviation'] = std_dv
    calculations['max'] = max_v
    calculations['min'] = min_v
    calculations['sum'] = sum_v

    return calculations


print(calculate([0, 1, 2, 4, 5, 6, 7, 8]))
