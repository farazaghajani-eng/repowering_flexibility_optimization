# Dual-Consistent Flexibility Index (DCFI) Framework

**Core Idea**
This repository implements the **Dual-Consistent Flexibility Index (DCFI)**  a market-integrated metric derived from LMPs and transmission shadow prices to identify spatial and temporal flexibility scarcity.
The two-layer stochastic MILP closes the market-equilibrium loop between upper-level repowering investment decisions and lower-level stochastic SCED on the **IEEE 118-bus** test system using **Gurobi**.

**Key Features**
- Upper layer: Two-stage stochastic MILP for repowering decisions (binary variables for ramp enhancement, min-output reduction, fuel-switching)
- Lower layer: Stochastic Security-Constrained Economic Dispatch (DCOPF-based) with endogenous dual extraction
- DCFI computation from dual variables (LMPs + shadow prices)
- Market equilibrium feedback loop
- Full uncertainty modeling (renewables, load, fuel prices)
- Ready for IEEE Transactions on Power Systems submission

**Dependencies**
- gurobipy (>=10.0)
- numpy, pandas, scipy
- pyomo or direct gurobipy
- matplotlib, seaborn (for visualization)

**Citation** (planned)
Author et al., "Dual-Consistent Flexibility Index for Guiding Generator Repowering in Congested Power Systems," IEEE Trans. Power Syst., 202X.
