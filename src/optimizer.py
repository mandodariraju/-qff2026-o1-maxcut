import numpy as np
from scipy.optimize import minimize
from qiskit.quantum_info import Statevector
from src.qaoa_circuit import build_qaoa_circuit

# Reduced graph edges and linear terms weights for expected cut calculation
edges = [(0, 1, 1), (0, 2, 5), (1, 2, 1), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 4, 1), (3, 4, 4)]
linear_terms = {0: 2, 1: 5, 2: 4, 3: 4}

def compute_expected_cut(params):
    gamma, beta = params
    qc = build_qaoa_circuit(gamma, beta)
    sv = Statevector(qc)
    probs = sv.probabilities_dict()

    total_cut = 0.0
    for bitstr, prob in probs.items():
        # bitstr is little-endian (q0 to q4)
        # Add fixed vertex 4 value = 1 (complement symmetry will handle the other)
        full_bits = [int(b) for b in bitstr] + [1] # vertex 4 fixed to 1

        # Calculate cut value for this 6-bit string
        cut = 0
        for u, v, w in edges + [(0,4,2), (1,4,5), (2,4,1), (3,4,4)]: # including edges with vertex 4
            if full_bits[u] != full_bits[v]:
                cut += w
        total_cut += cut * prob
    return -total_cut # Negative because we want to maximize cut

# Run COBYLA optimization with multiple random initial points
best_res = None
best_val = 0
for seed in range(3):
    np.random.seed(seed)
    init_params = np.random.uniform(0, 2*np.pi, 2)
    res = minimize(compute_expected_cut, init_params, method='COBYLA', options={'maxiter': 100})
    if -res.fun > best_val:
        best_val = -res.fun
        best_res = res

print(f"Optimal Expected Cut: {best_val:.2f}")
print(f"Best Parameters (gamma, beta): {best_res.x}")
