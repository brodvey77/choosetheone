from duty import duty
from math import ceil

def nds(value):
    return ceil(((value + duty(value)) * 20) / 100)
