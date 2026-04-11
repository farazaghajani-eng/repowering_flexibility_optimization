# Repowering Flexibility Optimization

## Overview

This repository presents a reproducible research framework developed as part of an M.Sc. thesis in Power Systems at the University of Tehran.

The project investigates the **technical and economic feasibility of repowering aging power plants** to enhance flexibility in modern power systems with high penetration of renewable energy.

The work is extended with a **stochastic optimization framework for flexibility, reserves, and investment decisions**, aligned with current EU research directions.

---

## Reproducibility & CI

This repository includes a **GitHub Actions Continuous Integration (CI) pipeline** that ensures reproducibility in a controlled environment.

The CI workflow:

- Installs all required dependencies
- Verifies core libraries (Pyomo, pandas, numpy)
- Executes a **lightweight deterministic model (`journal_run.py`)**
- Validates solver functionality in a clean environment

⚠️ Note:
Full-scale IEEE-118 simulations are **not executed in CI** due to computational and solver limitations (Gurobi, large-scale optimization).

---

## Repository Structure

- `IEEE118_Repowering_Analysis.md` → Full system-level analysis
- `Journal_Game_Space.ipynb` → Complete experimental implementation
- `journal_run.py` → Minimal executable model for CI validation
- `/Results` → Figures and output summaries

---

## Methodology

1. **Data Preparation**
   - IEEE-118 bus system data
   - Scenario-based stress testing (12,000 MW)
   - Demand flexibility envelope construction

2. **Modeling & Simulation**
   - Network-constrained unit commitment
   - Repowering investment decisions
   - Flexibility and reserve co-optimization

3. **Analysis**
   - Cost evaluation
   - Dispatch behavior
   - Nodal price formation (LMPs)

4. **Validation**
   - System feasibility under stress conditions
   - Congestion-driven price separation
   - Investment alignment with scarcity signals

---

## Key Results

- System load shedding: **1,158.66 MW**
- Reserve shortage: **741.33 MW**
- LMP range: **$22/MW – $5000/MW (VOLL cap)**
- Repowering driven by **nodal congestion signals**

---

## Solver & Pricing

Final results were obtained using **Gurobi (Fixed-LP formulation)** to ensure:

- Reliable extraction of Locational Marginal Prices (LMPs)
- Correct representation of congestion and scarcity pricing

---

## Validation Checks

- ✅ Feasible under extreme system stress
- ✅ Scarcity prices reach VOLL cap
- ✅ Congestion creates nodal price separation
- ✅ Investment aligns with high-LMP nodes
- ✅ CI pipeline validates core executable model

---

## Final Confirmation

The repository is:

- ✔ Structurally complete
- ✔ Economically consistent
- ✔ Reproducible via CI-validated workflow
- ✔ Aligned with EU research on flexibility, congestion, and nodal pricing

This repository is ready for:

- PhD applications (DTU, TU Delft, ETH, KU Leuven)
- Academic review
- Journal extension
