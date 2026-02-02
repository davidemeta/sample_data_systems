import numpy as np
from scipy import signal
from .utils import poly_mul, poly_sub, poly_add, roots_to_poly

def calculate_stabilizing_controllers(num_P, den_P, T):
    poles = np.roots(den_P)
    unstable_indices = np.where(np.abs(poles) >= 1.0 - 1e-5)[0]
    
    if len(unstable_indices) == 0:
        return ([0.0], [1.0]), ([1.0], [1.0]), ([1.0], [1.0]), (num_P, den_P), True

    else:
        zeros = np.roots(num_P)
        p_unst = poles[np.abs(poles) >= 1.0 - 1e-5]
        p_stab = poles[np.abs(poles) < 1.0 - 1e-5]
        z_unst = zeros[np.abs(zeros) >= 1.0 - 1e-5]
        z_stab = zeros[np.abs(zeros) < 1.0 - 1e-5]

        A_plus = roots_to_poly(p_unst)
        A_minus = roots_to_poly(p_stab)
        B_plus = roots_to_poly(z_unst)
        B_minus_monic = roots_to_poly(z_stab)

        reconstructed = poly_mul(B_plus, B_minus_monic)
        idx = next((i for i, x in enumerate(num_P) if abs(x) > 1e-10), 0)
        k_gain = num_P[idx] / reconstructed[0] if len(reconstructed)>0 else 1.0
        B_minus = k_gain * B_minus_monic

        nP = len(p_unst)
        nZ = len(z_unst)
        E = max(1, (len(den_P)-1) - (len(num_P)-1))
        deg_den_W = nP + nZ + E - 1

        # Calcolo F(z)
        if nP == 1:     
            p = p_unst[0]
            b_val = np.polyval(B_plus, p)
            f0 = (p ** deg_den_W) / b_val
            F_poly = np.array([f0])
        else:
            M_matrix = []
            b_vector = []
            for p in p_unst:
                rhs = (p ** deg_den_W) / np.polyval(B_plus, p)
                b_vector.append(rhs)
                row = [p**k for k in range(nP)]
                M_matrix.append(row)
            try:
                F_poly = np.linalg.solve(M_matrix, b_vector)[::-1]
            except:
                F_poly = np.linalg.lstsq(M_matrix, b_vector, rcond=None)[0][::-1]

        # Calcolo W(z) e H(z)
        W_num = poly_mul(B_plus, F_poly)
        z_pow_W = np.zeros(deg_den_W + 1); z_pow_W[0] = 1.0
        
        diff_poly = poly_sub(z_pow_W, W_num)
        H_num, remainder = signal.deconvolve(diff_poly, A_plus)
        
        # Check resto
        if np.max(np.abs(remainder)) > 1e-4:
            print(f"[WARN] Resto divisione H(z) non nullo: {np.max(np.abs(remainder))}")

        z_pow_nP = np.zeros(nP + 1); z_pow_nP[0] = 1.0
        deg_XY = nZ + E - 1
        z_pow_XY = np.zeros(deg_XY + 1); z_pow_XY[0] = 1.0
        
        M = (A_plus, z_pow_nP)
        N = (poly_mul(B_plus, B_minus), poly_mul(A_minus, z_pow_nP))
        X = (poly_mul(A_minus, F_poly), poly_mul(B_minus, z_pow_XY))
        Y = (H_num, z_pow_XY)

        return X, Y, M, N, False

def compute_Cd_generic(X, Y, M, N, Q, is_stable):
    Qn, Qd = Q
    if is_stable:
        Pn, Pd = N
        num_final = poly_mul(Qn, Pd)
        den_final = poly_sub(poly_mul(Qd, Pd), poly_mul(Pn, Qn))
    else:
        Xn, Xd = X; Yn, Yd = Y
        Mn, Md = M; Nn, Nd = N
        
        num_top = poly_add(poly_mul(Xn, poly_mul(Md, Qd)), poly_mul(Mn, poly_mul(Qn, Xd)))
        den_top = poly_mul(Xd, poly_mul(Md, Qd))
        num_bot = poly_sub(poly_mul(Yn, poly_mul(Nd, Qd)), poly_mul(Nn, poly_mul(Qn, Yd)))
        den_bot = poly_mul(Yd, poly_mul(Nd, Qd))
        
        num_final = poly_mul(num_top, den_bot)
        den_final = poly_mul(den_top, num_bot)

    return num_final, den_final