import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Calcola Pd(z) per P(s) = 1/(s+a)
def get_discrete_sys_case1(a, T):
    
    if a == 0:
        # Caso a=0: 1/s -> T / (z-1)
        return [T], [1, -1]
    else:
        # Caso a!=0: (1 - exp(-aT))/a / (z - exp(-aT))
        val = np.exp(-a * T)
        k = (1 - val) / a
        return [k], [1, -val]

#Calcola Pd(z) per P(s) = 1/(s(s+a))
def get_discrete_sys_case2(a, T):
    
    # Pd(z) = [ (aT - 1 + e^-aT)z + (1 - e^-aT - aTe^-aT) ] / [ a^2 (z-1)(z-e^-aT) ]
    e_at = np.exp(-a * T)
    term1 = a * T - 1 + e_at
    term2 = 1 - e_at - a * T * e_at
    
    num = [term1 / (a**2), term2 / (a**2)]
    den = [1, -(1 + e_at), e_at]
    
    return num, den

#Calcola Pd(z) per P(s) = (s+b)/(s(s+a))
def get_discrete_sys_case3(a, b, T):

    e_at = np.exp(-a * T)
    den = [1, -(1 + e_at), e_at]
    
    c1_z1 = a * (1 - e_at)
    c1_z0 = -a * (1 - e_at) 
    
    c2_z1 = b * (a * T - 1 + e_at)
    c2_z0 = b * (1 - e_at - a * T * e_at)
    
    num = [(c1_z1 + c2_z1) / (a**2), (c1_z0 + c2_z0) / (a**2)]
    
    return num, den