import os
import pandas as pd
from qiskit import transpile
from src.qaoa_circuit import build_qaoa_circuit
from src.processors import load_processor_config

# Load processors A and B
proc_a = load_processor_config("processors/processor_A.json")
proc_b = load_processor_config("processors/processor_B.json")

qc = build_qaoa_circuit(gamma=2.62, beta=5.54)

results = []
for proc_name, backend in [("Processor_A", proc_a), ("Processor_B", proc_b)]:
    for seed in range(20):
        t_qc = transpile(qc, backend=backend, optimization_level=3, seed_transpiler=seed)
        op_counts = t_qc.count_ops()
        cx_count = op_counts.get('cx', 0)
        swap_count = op_counts.get('swap', 0)
        effective_cx = cx_count + 3 * swap_count
        
        results.append({
            "Processor": proc_name,
            "Seed": seed,
            "Depth": t_qc.depth(),
            "CX": cx_count,
            "SWAP": swap_count,
            "Effective_CX": effective_cx,
            "Qubits_Used": len(t_qc.active_ancillas) if hasattr(t_qc, 'active_ancillas') else 5
        })

os.makedirs("results/tables", exist_ok=True)
df = pd.DataFrame(results)
df.to_csv("results/tables/transpile_summary.csv", index=False)
print("Transpile study complete! Summary saved to results/tables/transpile_summary.csv")
print(df.groupby("Processor")[["Depth", "Effective_CX"]].mean())
