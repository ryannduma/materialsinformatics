# Import the screening functions
from __future__ import annotations

from stoichiometry_screening import binary_screening, quaternary_screening, ternary_screening

# Binary screening
binary_elements = ["Na", "Cl", "K", "Br"]
df_bin = binary_screening(binary_elements, max_stoich=4)

# Ternary screening (e.g., perovskites)
elements_ternary = ["Ca", "Ti", "O"]
df_tern = ternary_screening(elements_ternary, ratio=(1, 1, 3), max_mult=2)

# Quaternary screening
elements_quad = ["Cu", "Ti", "O", "N"]
df_quad = quaternary_screening(elements_quad, max_stoich=2)
