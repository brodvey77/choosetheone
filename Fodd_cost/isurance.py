from start import cost_of_invoice
from math import ceil

def cost_of_insurance():
    return ceil((cost_of_invoice * 0.2) / 100)

cost_of_insurance(cost_of_invoice)