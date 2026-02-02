import numpy as np

def get_discrete_sys_case1(a, T, K):
    if a == 0: return [K*T], [1, -1]
    alpha = np.exp(-a*T)
    return [(K/a)*(1-alpha)], [1, -alpha]

def get_discrete_sys_case2(a, T, K):
    alpha = np.exp(-a*T)
    lam = (K/(a**2)) * (a*T - 1 + alpha)
    beta = (K/(a**2)) * (1 - alpha - a*T*alpha)
    return [lam, beta], [1, -(1+alpha), alpha]

def get_discrete_sys_case3(a, b, T, K):
    alpha = np.exp(-a*T)
    common = (a - b) * (1 - alpha)
    lam = (K/(a**2)) * (common + b*a*T)
    beta = -(K/(a**2)) * (common + b*a*T*alpha)
    return [lam, beta], [1, -(1+alpha), alpha]

def get_Pd_from_input(case, a, b, K, T):
    if case == 1:   return get_discrete_sys_case1(a, T, K)
    elif case == 2: return get_discrete_sys_case2(a, T, K)
    elif case == 3: return get_discrete_sys_case3(a, b, T, K)
    else: return [0], [1]