import numpy as np
def ADG(length, period):
    constant = 4*(np.pi**2)
    ratio = length/(period**2)
    return constant*ratio

def ADGUncertainty(length, period, lengthUncertainty, periodUncertainty):
    acceleration = ADG(length, period)
    uncertainty = ((2*periodUncertainty)/period+(lengthUncertainty/length))
    return acceleration*uncertainty
