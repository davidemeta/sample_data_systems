import numpy as np

def poly_mul(p1, p2):
    return np.convolve(p1, p2)

def poly_add(p1, p2):
    return np.polyadd(p1, p2)

def poly_sub(p1, p2):
    return np.polysub(p1, p2)

def roots_to_poly(roots):
    if len(roots) == 0: return np.array([1.0])
    return np.poly(roots)

def format_poly_string(coeffs):
    coeffs = np.where(np.abs(coeffs) < 1e-5, 0, coeffs)
    
    if np.all(coeffs == 0):
        return "0"

    terms = []
    degree = len(coeffs) - 1
    
    first_term = True
    
    for i, c in enumerate(coeffs):
        power = degree - i
        if c == 0:
            continue
        if first_term:
            sign = "" if c > 0 else "-"
            first_term = False
        else:
            sign = " + " if c > 0 else " - "
        
        abs_c = abs(c)
        val_str = f"{abs_c:.4f}"

        if power == 0:
            z_str = ""
        elif power == 1:
            z_str = "z"
        else:
            z_str = f"z^{power}"
            
        terms.append(f"{sign}{val_str}{z_str}")
        
    return "".join(terms)

def print_result(name, num, den):
    num_str = format_poly_string(num)
    den_str = format_poly_string(den)
    width = max(len(num_str), len(den_str))
    padding = 4
    line = "-" * width
    
    print(f"\n{name} =")
    print(f"{' ' * padding}{num_str.center(width)}")
    print(f"{' ' * padding}{line}")
    print(f"{' ' * padding}{den_str.center(width)}")