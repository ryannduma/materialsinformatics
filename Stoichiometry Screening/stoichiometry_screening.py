"""
Comprehensive stoichiometry screening module for materials discovery using SMACT.

This module provides tools for systematic exploration of chemical spaces through:
- Binary compound screening
- Ternary compound screening (including ABX₃)
- Quaternary compound screening
- Integration with Materials Project
- Advanced visualization

Author: [Ry Nduma]
Date: [Friday/17th/Jan/2025]
"""

from __future__ import annotations

import itertools
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from mp_api.client import MPRester

# For parallel processing
from pandarallel import pandarallel
from pymatgen.core import Composition

# SMACT imports
from smact import Species
from smact.oxidation_states import Oxidation_state_probability_finder
from smact.screening import smact_validity
from smact.utils.oxidation import ICSD24OxStatesFilter

pandarallel.initialize(progress_bar=True)

###############################################################################
# Helper Functions
###############################################################################


def generate_compositions(elements, ratio, max_mult=2):
    """Generate compositions for a fixed stoichiometric ratio.

    Args:
        elements (list[str]): List of element symbols
        ratio (list[int]): The stoichiometric ratio
        max_mult (int): Maximum scaling factor

    Returns:
        list[Composition]: List of reduced compositions
    """
    compositions = []
    for mult in range(1, max_mult + 1):
        stoich = [r * mult for r in ratio]
        comp_dict = dict(zip(elements, stoich, strict=False))
        comp = Composition(comp_dict).reduced_composition
        compositions.append(comp)
    return list(set(compositions))


def get_all_chem_sys(elements):
    """Get all possible chemical subsystems.

    Args:
        elements (str | list[str]): Elements or chemical system

    Returns:
        list[str]: All possible subsystems
    """
    if isinstance(elements, str):
        elements = elements.split("-")

    elements_set = set(elements)
    all_chemsys = []

    for i in range(len(elements_set)):
        for els in itertools.combinations(elements_set, i + 1):
            all_chemsys.append("-".join(sorted(els)))

    return all_chemsys


###############################################################################
# Binary Screening
###############################################################################


def binary_screening(element_list, max_stoich=5):
    """Screen binary compositions for validity.

    Args:
        element_list (list): List of elements to screen
        max_stoich (int): Maximum stoichiometry to consider

    Returns:
        pd.DataFrame: Results of binary screening
    """
    results = []

    for A, B in itertools.combinations(element_list, 2):
        for x in range(1, max_stoich + 1):
            for y in range(1, max_stoich + 1):
                comp = Composition({A: x, B: y}).reduced_composition
                valid = smact_validity(comp)
                results.append(
                    {
                        "pair": f"{A}-{B}",
                        "composition": comp,
                        "reduced_formula": comp.reduced_formula,
                        "valid_smact": valid,
                    }
                )

    df = pd.DataFrame(results).drop_duplicates("reduced_formula").reset_index(drop=True)
    return df


def plot_binary_grid(df_binary, pair="Na-Cl", max_stoich=5):
    """Plot a binary composition grid showing valid stoichiometries.

    Args:
        df_binary (pd.DataFrame): DataFrame with binary screening results
        pair (str): Element pair to plot (e.g. 'Na-Cl')
        max_stoich (int): Maximum stoichiometry to show
    """
    subdf = df_binary[df_binary["pair"] == pair].copy()
    A, B = pair.split("-")

    grid = np.zeros((max_stoich, max_stoich), dtype=int)

    for _, row in subdf.iterrows():
        comp = row["composition"]
        countA = int(comp[A])
        countB = int(comp[B])
        grid[countA - 1, countB - 1] = 1 if row["valid_smact"] else -1

    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.matshow(grid, cmap="RdYlGn", origin="lower")

    for i in range(max_stoich):
        for j in range(max_stoich):
            val = grid[i, j]
            text = "✓" if val == 1 else "×" if val == -1 else ""
            ax.text(j, i, text, va="center", ha="center", color="black", fontsize=14)

    ax.set_xlabel(f"{B} stoichiometric coefficient")
    ax.set_ylabel(f"{A} stoichiometric coefficient")
    ax.set_title(f"SMACT Validity Grid for {pair}")
    plt.colorbar(cax, ax=ax, label="1=Valid, -1=Invalid, 0=Unused")
    plt.show()


###############################################################################
# Ternary Screening
###############################################################################


def ternary_screening(elements_triplet, ratio=(1, 1, 3), max_mult=2):
    """Screen ternary compositions for a given stoichiometry ratio.

    Args:
        elements_triplet (list): Three elements to screen
        ratio (tuple): Target stoichiometry ratio (default: ABX₃)
        max_mult (int): Maximum multiplier for the ratio

    Returns:
        pd.DataFrame: Results of ternary screening
    """
    comps = generate_compositions(elements_triplet, ratio=ratio, max_mult=max_mult)

    data = []
    for c in comps:
        data.append(
            {
                "elements_triplet": "-".join(elements_triplet),
                "composition": c,
                "reduced_formula": c.reduced_formula,
                "valid_smact": smact_validity(c),
            }
        )
    return pd.DataFrame(data)


def plot_ternary(df, elements):
    """Create an interactive ternary plot of compositions.

    Args:
        df (pd.DataFrame): DataFrame with composition data
        elements (list): List of elements to plot
    """

    def comp_to_frac(comp):
        amounts = [comp[el] for el in elements]
        total = sum(amounts)
        return [amt / total for amt in amounts]

    fracs = np.array([comp_to_frac(row["composition"]) for _, row in df.iterrows()])

    fig = go.Figure()

    # Add valid compositions
    valid_mask = df["valid_smact"]
    if valid_mask.any():
        valid_fracs = fracs[valid_mask]
        fig.add_trace(
            go.Scatterternary(
                a=valid_fracs[:, 0],
                b=valid_fracs[:, 1],
                c=valid_fracs[:, 2],
                mode="markers",
                marker=dict(size=10, color="green", symbol="circle"),
                name="Valid",
            )
        )

    # Add invalid compositions
    invalid_mask = ~valid_mask
    if invalid_mask.any():
        invalid_fracs = fracs[invalid_mask]
        fig.add_trace(
            go.Scatterternary(
                a=invalid_fracs[:, 0],
                b=invalid_fracs[:, 1],
                c=invalid_fracs[:, 2],
                mode="markers",
                marker=dict(size=10, color="red", symbol="x"),
                name="Invalid",
            )
        )

    fig.update_layout(
        title=f"Ternary Composition Space: {'-'.join(elements)}",
        ternary=dict(aaxis=dict(title=elements[0]), baxis=dict(title=elements[1]), caxis=dict(title=elements[2])),
    )

    fig.show()


###############################################################################
# Quaternary Screening
###############################################################################


def quaternary_screening(elements_quad, max_stoich=3):
    """Screen quaternary compositions.

    Args:
        elements_quad (list): Four elements to screen
        max_stoich (int): Maximum stoichiometry to consider

    Returns:
        pd.DataFrame: Results of quaternary screening
    """
    results = []

    for x, y, z, w in itertools.product(range(1, max_stoich + 1), repeat=4):
        comp_dict = dict(zip(elements_quad, [x, y, z, w], strict=False))
        comp = Composition(comp_dict).reduced_composition

        valid = smact_validity(comp)
        results.append(
            {
                "quad": "-".join(elements_quad),
                "composition": comp,
                "reduced_formula": comp.reduced_formula,
                "valid_smact": valid,
            }
        )

    df = pd.DataFrame(results).drop_duplicates("reduced_formula").reset_index(drop=True)
    return df


###############################################################################
# Materials Project Integration
###############################################################################


def query_materials_project(elements, api_key=None):
    """Query the Materials Project database for known compounds.

    Args:
        elements (list[str]): Elements to search for
        api_key (str): Materials Project API key

    Returns:
        list[Composition]: Known compositions from MP
    """
    if api_key is None:
        api_key = os.environ.get("MP_API_KEY")
        if api_key is None:
            raise ValueError("No Materials Project API key provided")

    all_chemsys = get_all_chem_sys(elements)

    with MPRester(api_key) as mpr:
        mp_entries = mpr.materials.summary.search(chemsys=all_chemsys)

    return [entry.composition.reduced_composition for entry in mp_entries]


###############################################################################
# Advanced Analysis
###############################################################################


def analyze_oxidation_states(compositions, threshold=50):
    """Analyze oxidation states using ICSD data.

    Args:
        compositions (list[Composition]): Compositions to analyze
        threshold (int): Minimum number of ICSD occurrences

    Returns:
        pd.DataFrame: Analysis results
    """
    ox_filter = ICSD24OxStatesFilter()
    ox_prob_finder = Oxidation_state_probability_finder()

    results = []
    for comp in compositions:
        # Get possible oxidation states
        species_list = []
        for el in comp.elements:
            ox_states = ox_filter.get_oxidation_states(el.symbol, threshold=threshold)
            if ox_states:
                species_list.extend([Species(el.symbol, ox) for ox in ox_states])

        # Calculate probability if species found
        if species_list:
            prob = ox_prob_finder.compound_probability(species_list)
        else:
            prob = 0.0

        results.append({"composition": comp, "formula": comp.reduced_formula, "oxidation_probability": prob})

    return pd.DataFrame(results)


if __name__ == "__main__":
    # Example usage
    print("Running example stoichiometry screening...")

    # Binary example
    binary_elements = ["Na", "Cl", "K", "Br"]
    df_bin = binary_screening(binary_elements, max_stoich=4)
    print("\nBinary screening results:")
    print(df_bin.head())

    # Ternary example (perovskite-like)
    elements_ternary = ["Ca", "Ti", "O"]
    df_tern = ternary_screening(elements_ternary, ratio=(1, 1, 3), max_mult=2)
    print("\nTernary (ABX₃) screening results:")
    print(df_tern)

    # Quaternary example
    elements_quad = ["Cu", "Ti", "O", "N"]
    df_quad = quaternary_screening(elements_quad, max_stoich=2)
    print("\nQuaternary screening results:")
    print(df_quad.head())
