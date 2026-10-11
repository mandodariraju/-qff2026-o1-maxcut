import os
import pandas as pd
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel
from src.qaoa_circuit import build_qaoa_circuit
from src.processors import load_processor, build_noise_model, build_coupling_map

# Load processors
proc_a = load_processor("processors/processor_A.json")
proc_b = load_processor("processors/processor_B.json")

noise_a = build_noise_model(proc_a)
cmap_a = build_coupling_map(proc_a)

noise_b = build_noise_model(proc_b)
cmap_b = build_coupling_map(proc_b)

qc = build_qaoa_circuit(gamma=2.62, beta=5.54)
qc.measure_all()

# Transpile and simulate with noise
results = []
for name, backend_config, noise_m, cmap in [("Case_A2_Noisy", proc_a, noise_a, cmap_a), ("Case_B2_Noisy", proc_b, noise_b, cmap_b)]:
    sim = AerSimulator(noise_model=noise_m)
    t_qc = transpile(qc, coupling_map=cmap, optimization_level=3)
    
    job = sim.run(t_qc, shots=1024)
    counts = job.result().get_counts()
    
    results.append({
        "Case": name,
        "Total_Shots": 1024,
        "Unique_Bitstrings": len(counts)
    })

os.makedirs("results/tables", exist_ok=True)
df = pd.DataFrame(results)
df.to_csv("results/tables/quality_summary.csv", index=False)
print("Noisy simulation complete! Summary saved to results/tables/quality_summary.csv")
print(df)
