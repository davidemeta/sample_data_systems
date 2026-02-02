from src.pd_z import get_Pd_from_input
from src.cd_z import calculate_stabilizing_controllers, compute_Cd_generic
from src.utils import print_result

if __name__ == "__main__":
    
    # 1. Setup Parametri
    CASE = 3
    a_val = -1.0 
    b_val = 2.0
    T_val = 0.1
    K_val = 1.0
    
    # 2. Ottieni Pd(z)
    pd_num, pd_den = get_Pd_from_input(CASE, a_val, b_val, K_val, T_val)
    print_result("Impianto Pd(z)", pd_num, pd_den)
    
    # 3. Ottini X, Y, M, N per Cd(z)
    X, Y, M, N, is_stable = calculate_stabilizing_controllers(pd_num, pd_den, T_val)
    
    # 4. Scegli Q(z)
    Q = ([5.0], [1.0])
    
    # 5. Calcola Cd(z)
    cd_num, cd_den = compute_Cd_generic(X, Y, M, N, Q, is_stable)
    
    # 6. Output Finale
    print_result("Controllore Stabilizzante Cd(z)", cd_num, cd_den)