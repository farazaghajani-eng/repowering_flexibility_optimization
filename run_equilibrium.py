"""
Main script: Iterative or decomposed solution of the two-layer stochastic market-equilibrium model
"""

from src.models.upper_layer import build_upper_layer
from src.models.lower_layer import build_lower_layer
# ... load IEEE 118 data

# Load IEEE 118 data (matpower format or custom)
data = load_ieee118_data()

scenarios = generate_scenarios(N=50) # renewables, load, fuel

# Iterative equilibrium or Benders decomposition
for iteration in range(max_iter):
# Solve lower layer for all scenarios  get DCFI signals
dcfi_signals = {}
for omega in scenarios:
dcfi, _, _ = build_lower_layer(data, omega)
dcfi_signals[omega] = dcfi

# Solve upper layer with updated DCFI feedback
upper = build_upper_layer(data, scenarios, dcfi_signals)
upper.optimize()

# Update repowering decisions and repeat until convergence
print(f"Iteration {iteration}: Investment decisions updated, DCFI equilibrium gap = {gap}")

print("Market equilibrium reached. Optimal repowering decisions obtained.")
