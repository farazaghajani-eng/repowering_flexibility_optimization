"""
Dual-Consistent Flexibility Index (DCFI)
Derived from LMPs (?) and constraint shadow prices (µ)
"""

def compute_dcfi(LMP, mu_pos, mu_neg, data):
DCFI = {}
for n in data.nodes:
for t in data.time:
congestion_component = sum(mu_pos[line,t] + mu_neg[line,t] for line in data.incident_lines(n))
DCFI[(n,t)] = LMP[n][t] + data.alpha * congestion_component + data.beta * data.flex_dual_term(n,t)
return DCFI
