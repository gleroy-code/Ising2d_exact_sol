import math
from scipy.special import ellipk

def energy(x):
    '''
    input : x = k_BT/J
    output : E/(NJ) exact energy density for PBC Ising model in thermo limit 
    '''
    kappa = (math.sinh(2/x)) / (2*(1+math.sinh(2/x)**2))
    energy = (-1 / math.tanh(2/x)) * (1 - 2 * math.tanh(2 / x)**2 * (2 / math.pi) * ellipk(16 * kappa**2)) 
    return energy
