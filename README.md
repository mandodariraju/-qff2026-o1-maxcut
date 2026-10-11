# -qff2026-o1-maxcut
Project Q (QFF 2026) Phase 1, PS-O1: Weighted Max-Cut with QAOA, benchmarked on Processor A (5 qubits) and Processor B (9 qubits) with SWAP and routing analysis.
# QFF 2026 Phase 1: PS-O1 Max-Cut on Weighted Graphs

**Team:** [Garuda]
**Problem:** Quantum Optimization, PS-O1 Max-Cut
**Method:** QAOA, benchmarked on Processor A (5 qubits) and Processor B (9 qubits) with SWAP and routing analysis.

## Assumptions (provisional)
- Processor maps from the Processor A/B Benchmark Configuration PDF (marked "For Organizer Approval").
- Noise: values in `processors/*.json` (provisional until organizers confirm).
- Processor A has 5 qubits and the graph has 6 vertices, so one vertex is fixed for the reduced 5-variable problem.

## Setup
```
pip install -r requirements.txt
```

## How to run
Open `main.ipynb` and run all cells top to bottom. Results are saved in `results/tables` and `results/figures`.

## Methodology
(Short summary: cost Hamiltonian, QAOA depth, optimizer, transpilation seeds, cases A1/A2/B1/B2.)

## Key results
(Fill after the runs. Link to `report.md`.)

## Repository structure
`data/`, `processors/`, `src/`, `results/`, `main.ipynb`, `report.md`

## Limitations
(See `report.md`.)

An AI assistant was used for planning, debugging help, documentation structure, and for the classical helper code (src/problem.py, src/routing.py). The QAOA circuit construction and the optimization loop were implemented by the team.
