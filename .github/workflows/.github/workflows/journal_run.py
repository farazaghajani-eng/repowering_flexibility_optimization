import pyomo.environ as pyo

print("Running Journal Game Space model (CI version)...")

# --- Minimal test version (fast & deterministic) ---
T = range(3)
G = ["gen1"]
Omega = ["test"]

demand = {("test", t): 100 for t in T}

m = pyo.ConcreteModel()

m.T = pyo.Set(initialize=T)
m.G = pyo.Set(initialize=G)
m.Omega = pyo.Set(initialize=Omega)

m.p = pyo.Var(m.G, m.T, m.Omega, within=pyo.NonNegativeReals)

def obj_rule(m):
    return sum(m.p[g, t, w] for g in m.G for t in m.T for w in m.Omega)

m.obj = pyo.Objective(rule=obj_rule)

def balance_rule(m, t, w):
    return sum(m.p[g, t, w] for g in m.G) >= demand[(w, t)]

m.balance = pyo.Constraint(m.T, m.Omega, rule=balance_rule)

solver = pyo.SolverFactory("glpk")
results = solver.solve(m)

print("Status:", results.solver.status)
print("Termination:", results.solver.termination_condition)

assert str(results.solver.termination_condition) == "optimal"

print("CI test passed ✅")
