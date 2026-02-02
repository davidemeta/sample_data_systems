import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Calcola Pd(z) per P(s) = K / (s+a)
# Formula: Pd(z) = beta / (z - alpha)
def get_discrete_sys_case1(a, T, K=1.0):
    
    if a == 0:
        beta = K * T
        return [beta], [1, -1]
        
    else:
        alpha_val = np.exp(-a * T)
        beta = (K / a) * (1 - alpha_val)
        return [beta], [1, -alpha_val]

# Calcola Pd(z) per P(s) = K / (s(s+a))
# Formula: Pd(z) = (lambda*z + beta) / ((z-1)(z-alpha))
def get_discrete_sys_case2(a, T, K=1.0):
    
    alpha_val = np.exp(-a * T)
    lambda_val = (K / (a**2)) * (a * T - 1 + alpha_val)
    beta_val   = (K / (a**2)) * (1 - alpha_val - a * T * alpha_val)
    
    num = [lambda_val, beta_val]
    den = [1, -(1 + alpha_val), alpha_val]
    
    return num, den

# Calcola Pd(z) per P(s) = K(s+b) / (s(s+a))
# Formula: Pd(z) = (lambda*z + beta) / ((z-1)(z-alpha))
def get_discrete_sys_case3(a, b, T, K=1.0):

    alpha_val = np.exp(-a * T)
    common_term = (a - b) * (1 - alpha_val)
    lambda_val = (K / (a**2)) * (common_term + b * a * T)
    beta_val = -(K / (a**2)) * (common_term + b * a * T * alpha_val)
    
    num = [lambda_val, beta_val]
    den = [1, -(1 + alpha_val), alpha_val]
    
    return num, den

# --- PARAMETRI DI SIMULAZIONE ---
T = 0.1          # Tempo di campionamento (in secondi)
t_final = 5.0    # Durata simulazione
n_steps = int(t_final / T) + 1
K_val = 1.0      # Valore di K selezionato per la simulazione

# Creazione della figura
fig, axs = plt.subplots(3, 1, figsize=(10, 12))
plt.subplots_adjust(hspace=0.5)

# --- Caso 1 ---
axs[0].set_title(rf'Caso 1: $P(s) = \frac{{K}}{{s+a}}$  (con $K={K_val}$)', fontsize=12)
params1 = [(2, 'a=2 (Stabile)'), (0, 'a=0 (Integratore)'), (-0.5, 'a=-0.5 (Instabile)')]
for a, label in params1:
    num, den = get_discrete_sys_case1(a, T, K=K_val)
    t, y = signal.dstep((num, den, T), n=n_steps)
    axs[0].step(t, np.squeeze(y), where='post', label=label, linewidth=2)
axs[0].legend()
axs[0].grid(True, alpha=0.3)
axs[0].set_ylabel('Ampiezza')

# --- Caso 2 ---
axs[1].set_title(rf'Caso 2: $P(s) = \frac{{K}}{{s(s+a)}}$  (con $K={K_val}$)', fontsize=12)
params2 = [(2, 'a=2 (Stabile)'), (-0.5, 'a=-0.5 (Instabile)')]
for a, label in params2:
    num, den = get_discrete_sys_case2(a, T, K=K_val)
    t, y = signal.dstep((num, den, T), n=n_steps)
    axs[1].step(t, np.squeeze(y), where='post', label=label, linewidth=2)
axs[1].legend()
axs[1].grid(True, alpha=0.3)
axs[1].set_ylabel('Ampiezza')

# --- Caso 3 ---
axs[2].set_title(rf'Caso 3: $P(s) = \frac{{K(s+b)}}{{s(s+a)}}$ (con $a=1$ fisso, $K={K_val}$)', fontsize=12)
params3 = [(2, 'b=2 (Fase Minima)'), (-2, 'b=-2 (Fase Non Minima - Undershoot)')]
for b, label in params3:
    num, den = get_discrete_sys_case3(1, b, T, K=K_val)
    t, y = signal.dstep((num, den, T), n=n_steps)
    axs[2].step(t, np.squeeze(y), where='post', label=label, linewidth=2)
axs[2].legend()
axs[2].grid(True, alpha=0.3)
axs[2].set_ylabel('Ampiezza')
axs[2].set_xlabel('Tempo (s)')

plt.savefig('discrete_systems_analysis.png')
plt.show()