"""
Lower Layer: Stochastic Security-Constrained Economic Dispatch (SCED)
DC power flow on IEEE 118-bus, extract LMPs and shadow prices for DCFI
"""

import gurobipy as gp
from gurobipy import GRB

def build_lower_layer(data, scenario):
m = gp.Model("DCFI_Lower_SCED")
m.Params.OutputFlag = 0

# Variables: commitment, dispatch, angles, etc.
u = m.addVars(data.generators, data.time, vtype=GRB.BINARY, name="commit")
p = m.addVars(data.generators, data.time, lb=0, name="dispatch")
theta = m.addVars(data.nodes, data.time, lb=-GRB.INFINITY, name="angle")

# DC power flow constraints
for t in data.time:
for line in data.lines:
i, j = line
flow = data.B[line] * (theta[i,t] - theta[j,t])
m.addConstr(flow <= data.Fmax[line], f"line_{i}_{j}_pos")
m.addConstr(flow >= -data.Fmax[line], f"line_{i}_{j}_neg")

# Nodal balance (LMP dual will come from here)
for n in data.nodes:
for t in data.time:
gen_in_n = [g for g in data.generators if data.node[g] == n]
m.addConstr(
gp.quicksum(p[g,t] for g in gen_in_n) - data.demand[n,t,scenario]
+ data.renewable[n,t,scenario] ==
gp.quicksum(data.B[line]*(theta[i,t]-theta[j,t]) for line in data.incident_lines(n)),
name=f"balance_{n}_{t}"
)

# Objective: social welfare / generation cost
m.setObjective(gp.quicksum(data.cost[g] * p[g,t] for g in data.generators for t in data.time), GRB.MINIMIZE)

m.optimize()

if m.status == GRB.OPTIMAL:
# Extract duals for DCFI
LMP = {n: {t: m.getConstrByName(f"balance_{n}_{t}").Pi for t in data.time} for n in data.nodes}
shadow_pos = {}
shadow_neg = {}
# ... extract line shadow prices µ

dcfi = compute_dcfi(LMP, shadow_pos, shadow_neg, data)
return dcfi, LMP, m.objVal
return None, None, None
