import numpy as np

def calculate(pylist):
    # arr should contain 9 digits
    if len(pylist) < 9:
        raise ValueError ('List must contain nine numbers.')
    else:
        arr = np.array(pylist)

    # arr is reshaped to a 3 by 3 matrix.
    stats_array = arr.reshape((3,3))
    calculations = {
        'mean': [list(stats_array.mean(axis=0)), list(stats_array.mean(axis=1)), stats_array.mean()],
        'variance': [list(stats_array.var(axis=0)), list(stats_array.var(axis=1)), stats_array.var()],
        'standard deviation': [list(stats_array.std(axis=0)), list(stats_array.std(axis=1)), stats_array.std()],
        'max': [list(stats_array.max(axis=0)), list(stats_array.max(axis=1)), stats_array.max()],
        'min': [list(stats_array.min(axis=0)), list(stats_array.min(axis=1)), stats_array.min()],
        'sum': [list(stats_array.sum(axis=0)), list(stats_array.sum(axis=1)), stats_array.sum()],
    }
    return calculations