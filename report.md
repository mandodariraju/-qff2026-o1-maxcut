# Report: PS-O1 Max-Cut with QAOA on Processor A vs B

## 1. Problem
Weighted Max-Cut on a 6-vertex graph (weights 1-5). Objective: maximize the cut weight.

## 2. Method
- Cost Hamiltonian, QAOA depth p = ..., optimizer = ..., shots = ..., seeds = ...
- Reduction used for Processor A (5 qubits): [describe the fixed vertex]

## 3. Assumptions and setup
- Processor A / B definitions: processors/*.json (provisional, see README)
- Noise model: ...
- Transpiler: optimization_level = ..., number of seeds = ...

## 4. Results
### 4.1 Solution quality
| Case | Expected cut / optimum | P(optimal bitstring) | Best sampled cut |
|---|---|---|---|
| A1 (ideal) | | | |
| A2 (noisy) | | | |
| B1 (ideal) | | | |
| B2 (noisy) | | | |

### 4.2 Architecture metrics (mean ± std over seeds)
| Metric | Processor A | Processor B |
|---|---|---|
| Depth | | |
| Two-qubit gates | | |
| SWAP count | | |
| Physical qubits used | | |

## 5. Interpretation
1. What changed between A and B?
2. Which architectural property explains it (connectivity, hub qubits, cycles)?
3. How many extra operations did routing add?
4. Did the solution quality change, and by how much?
5. Could gate-set or noise differences also contribute?
6. What remains uncertain?

## 6. Limitations
- Simulated noise model only; provisional noise values.
- One graph instance family, finite topologies. No universal claim.

## 7. Conclusion
...
