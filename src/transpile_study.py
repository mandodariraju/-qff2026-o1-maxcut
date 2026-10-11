import os
import pandas as pd
from qiskit import transpile
from src.qaoa_circuit import build_qaoa_circuit
from src.processors import load_processor

# Load processors A and B using correct function
proc_a = load_processor("processors/processor_A.json")
proc_b = load_processor("processors/processor_B.json")

# Note: transpile takes backend or coupling map / target. Let's use Qiskit Aer backend or target from JSON if needed.
# For pure transpile study with coupling map:
from qiskit.transpiler import CouplingMap
cmap_a = CouplingMap(proc_a["coupling_map"])
cmap_b = CouplingMap(proc_b["coupling_map"])

qc = build_qaoa_circuit(gamma=2.62, beta=5.54)

results = []
for proc_name, cmap in [("Processor_A", cmap_a), ("Processor_B", cmap_b)]:
    for seed in range(20):
        t_qc = transpile(qc, coupling_map=cmap, optimization_level=3, seed_transpiler=seed)
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
