"""
Upper Layer: Two-stage stochastic MILP for generator repowering decisions
Objective: Min expected (investment + operation) + penalty on low DCFI
"""

import gurobipy as gp
from gurobipy import GRB
import numpy as np

def build_upper_layer(data, scenarios, dcfi_signals):
m = gp.Model("DCFI_Upper_Layer")

# First-stage: repowering binary decisions
x = m.addVars(data.generators, vtype=GRB.BINARY, name="repower_choice")

# Investment cost
invest_cost = gp.quicksum(data.inv_cost[g] * x[g] for g in data.generators)

# Expected operational cost + DCFI-weighted flexibility value (equilibrium term)
expected_op_cost = 0
flexibility_value = 0

for omega, prob in scenarios.items():
# Link to lower layer DCFI (pre-computed or via callback/Benders)
dcfi_omega = dcfi_signals[omega]
flexibility_value += prob * gp.quicksum(dcfi_omega[n] * data.flex_potential[g,n] * x[g]
for g in data.generators for n in data.nodes)

m.setObjective(invest_cost - flexibility_value + expected_op_cost, GRB.MINIMIZE)

# Budget and logical constraints
m.addConstr(gp.quicksum(x[g] for g in data.generators) <= data.budget, "budget")

m.Params.TimeLimit = 3600
m.Params.MIPGap = 0.001
return m
