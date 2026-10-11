from qiskit import QuantumCircuit
import numpy as np

def build_qaoa_circuit(gamma: float, beta: float) -> QuantumCircuit:
    # 5 qubits (vertex 4 fix chesaka migilina 5 variables kosam)
    qc = QuantumCircuit(5)
    
    # Step 1: Initial Hadamard Layer (Superposition)
    qc.h(range(5))
    
    # Step 2: Cost Layer (RZZ + RZ gates for the weighted graph & reduction terms)
    # Edges from reduced 5-node graph (vertex 4 fixed)
    # Format: (qubit_i, qubit_j, weight)
    edges = [
        (0, 1, 1), (0, 2, 5), (1, 2, 1), 
        (1, 3, 5), (1, 4, 5), (2, 3, 4), 
        (2, 4, 1), (3, 4, 4)
    ]
    for u, v, w in edges:
        qc.rzz(2 * gamma * w, u, v)
        
    # Linear terms (RZ gates) resulting from fixing vertex 4
    linear_terms = {0: 2, 1: 5, 2: 4, 3: 4}
    for q, coeff in linear_terms.items():
        qc.rz(2 * gamma * coeff, q)
        
    # Step 3: Mixer Layer (RX gates)
    for q in range(5):
        qc.rx(2 * beta, q)
        
    return qc

# Example usage with dummy angles:
qc = build_qaoa_circuit(gamma=0.5, beta=0.5)
print(f"Circuit Qubits: {qc.num_qubits}")
print(f"Circuit Depth: {qc.depth()}")
