# Thermodynamics in Materials Discovery

## Learning Objectives

After completing this section, you will be able to:

1. Understand basic thermodynamic principles in materials science
2. Apply thermodynamic concepts to predict material stability
3. Use computational tools to calculate thermodynamic properties
4. Interpret phase diagrams and stability plots

## Why Thermodynamics Matters

When we design new materials computationally, we're essentially asking: "If we could make this material, would it actually exist?" Thermodynamics gives us the tools to answer this question by telling us whether a material is stable, metastable, or will spontaneously decompose into other phases.

## Fundamental Thermodynamic Concepts

### Gibbs Free Energy: The Stability Scorecard

The Gibbs free energy (G) is arguably the most important quantity in materials thermodynamics. It combines the internal energy of a system with the effects of temperature and pressure:

$$G = H - TS$$

where:
- $H$ is the enthalpy (total heat content)
- $T$ is the temperature
- $S$ is the entropy (disorder)

**Why it matters**: Materials with lower Gibbs free energy are more stable. When comparing different possible structures or compositions, nature favors the configuration with the lowest G.

### Enthalpy: The Energy Budget

Enthalpy represents the total energy content of a material, including both internal energy and the work needed to make room for it:

$$H = U + PV$$

In computational materials science, we often work at constant pressure where volume changes are small, so enthalpy differences are approximately equal to energy differences calculated by DFT.

**Practical insight**: When DFT calculations give you the "formation energy" of a material, they're essentially giving you the enthalpy of formation at 0K.

### Entropy: The Disorder Factor

Entropy quantifies disorder in a system. While often overlooked in basic computational screening, entropy becomes crucial at high temperatures. There are several types of entropy in materials:

- **Configurational entropy**: Disorder from mixing different atoms on lattice sites
- **Vibrational entropy**: From thermal vibrations of atoms
- **Electronic entropy**: From thermal excitation of electrons

**Rule of thumb**: At room temperature, entropy effects typically contribute ~0.025 eV per atom to the free energy.

### Chemical Potential: The Driving Force

The chemical potential ($\mu$) represents the energy cost of adding one more atom of a particular element to the system:

$$\mu_i = \frac{\partial G}{\partial n_i}$$

This concept is crucial for understanding:
- Why materials decompose
- Which phases form under different conditions
- How materials exchange atoms with their environment

## Phase Stability: Will Your Material Survive?

### The Convex Hull: A Stability Map

The convex hull (often called the "ehull" or energy hull) is a geometric construction that identifies the most stable phases at each composition. Here's how it works:

1. Plot formation energies of all known phases vs. composition
2. Draw the lowest energy envelope connecting stable phases
3. Materials on the hull are stable; those above are unstable

**Energy above hull (Ehull)**: The vertical distance from a material to the hull indicates its instability:
- Ehull = 0: Thermodynamically stable
- 0 < Ehull < 25 meV/atom: Potentially synthesizable
- Ehull > 50 meV/atom: Likely unstable

### Reading Phase Diagrams

Phase diagrams map out which phases are stable under different conditions. For a binary system (A-B), you might see:

```
Temperature
    ^
    |  Liquid
    |--------
    |  A+B  |  B
    | solid | solid
    |_______|_______> Composition
    A              B
```

Key features to identify:
- **Single phase regions**: Only one structure is stable
- **Two-phase regions**: Material separates into two phases
- **Phase boundaries**: Where transitions occur

### Metastability: Kinetically Trapped States

Not all useful materials are thermodynamically stable! Many technologically important materials are metastable:

- **Diamond**: Metastable form of carbon (graphite is stable)
- **Many battery cathodes**: Delithiated states are often metastable
- **Amorphous materials**: Higher energy than crystals but kinetically trapped

**Practical consideration**: If Ehull < 50 meV/atom and there are high kinetic barriers to decomposition, the material might be synthesizable.

## Computational Methods for Thermodynamics

### DFT Energy Calculations

Density Functional Theory provides the foundation for computational thermodynamics:

1. **Total energy**: Direct output from DFT calculations
2. **Formation energy**: Energy relative to standard reference states
   $$E_f = E_{compound} - \sum n_i E_i^{ref}$$
3. **Mixing energy**: Energy change from mixing pure components

### The Materials Project Thermodynamics

The Materials Project provides thermodynamic data for ~150,000 materials:

```python
# Example: Getting thermodynamic data
from mp_api.client import MPRester

with MPRester("YOUR_API_KEY") as mpr:
    # Get thermodynamic data for Li-Fe-O system
    entries = mpr.get_entries_in_chemsys(["Li", "Fe", "O"])
    
    # Each entry contains:
    # - formation energy
    # - energy above hull
    # - equilibrium reaction energy
```

### Temperature Effects: Beyond 0K

Most DFT calculations are performed at 0K, but real applications need finite temperature properties:

1. **Vibrational contributions**: Use phonon calculations
   $$G_{vib} = \sum_{\mathbf{q},j} \left[\frac{\hbar\omega_{\mathbf{q}j}}{2} + k_BT\ln(1-e^{-\hbar\omega_{\mathbf{q}j}/k_BT})\right]$$

2. **Configurational entropy**: For disordered systems
   $$S_{config} = -k_B \sum_i x_i \ln(x_i)$$

3. **Electronic entropy**: Important for metals and small-gap semiconductors

### Pressure Effects

While often neglected in initial screening, pressure can dramatically affect stability:

- **Phase transitions**: Many materials transform under pressure
- **Synthesis conditions**: High-pressure synthesis can access metastable phases
- **Operational conditions**: Battery materials experience pressure during cycling

**Quick estimate**: Pressure contributes $PV$ to Gibbs energy. For typical solid volumes (~10 Å³/atom) and moderate pressures (1 GPa), this adds ~0.01 eV/atom.

## Practical Thermodynamic Screening

### Workflow for Stability Assessment

1. **Calculate formation energy** using DFT or retrieve from databases
2. **Construct convex hull** for the relevant chemical system
3. **Determine Ehull** for your target composition
4. **Check decomposition products** to understand failure modes
5. **Estimate temperature effects** if near stability boundary
6. **Consider synthesis conditions** that might stabilize the phase

### Rules of Thumb

- **Stable materials**: Ehull = 0 meV/atom
- **Synthesizable materials**: Ehull < 25-50 meV/atom
- **Temperature stabilization**: ~25 meV/atom per 300K from entropy
- **Polymorphs**: Often within 10-50 meV/atom of each other
- **Hydration/oxidation**: Check stability against H₂O and O₂

### Common Pitfalls

1. **Ignoring competing phases**: Always check the full phase diagram
2. **0K approximation**: Temperature can stabilize high-entropy phases
3. **Missing metastable phases**: Databases might not include all polymorphs
4. **Environmental stability**: Consider reaction with air/moisture

## Connecting to Other Course Concepts

Thermodynamics provides the foundation for understanding:
- **Why** certain compositions form (Chemical Filters section)
- **Which** structures are preferred (Structure Prediction section)
- **How** to design stable materials (Compositional Screening section)

In the next sections on DFT and MLFF, we'll see how these thermodynamic properties are actually calculated from first principles.

## Further Reading

- Computational Thermodynamics of Materials by Zi-Kui Liu
- "High-throughput screening of inorganic compounds for the discovery of novel dielectric and optical materials" by Petousis et al.
- Materials Project documentation on [thermodynamic stability](https://docs.materialsproject.org/methodology/thermodynamic-stability)