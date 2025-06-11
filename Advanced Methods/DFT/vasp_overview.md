# VASP: The Vienna Ab initio Simulation Package

## Introduction

VASP (Vienna Ab initio Simulation Package) is one of the most widely used software packages for performing ab initio quantum mechanical calculations using density functional theory (DFT). Developed at the University of Vienna, VASP has become a standard tool in computational materials science for studying the electronic structure and properties of materials.

## What is VASP?

VASP is a plane-wave DFT code that can:

- Calculate ground-state electronic structures
- Perform geometry optimisations
- Run molecular dynamics simulations
- Compute various materials properties
- Handle periodic systems effectively

### Key Features

1. **Efficiency**: Optimised algorithms for large-scale calculations
2. **Accuracy**: Implements current DFT methods
3. **Versatility**: Supports various functionals and calculation types
4. **Scalability**: Excellent parallel performance on HPC systems
5. **Reliability**: Thoroughly tested and validated

## Capabilities of VASP

### 1. Electronic Structure Calculations

- **Band Structures**: Complete electronic band diagrams
- **Density of States (DOS)**: Total and projected DOS
- **Charge Densities**: Spatial distribution of electrons
- **Work Functions**: Surface electronic properties
- **Fermi Surfaces**: For metallic systems

### 2. Structural Properties

- **Geometry Optimisation**: Finding equilibrium structures
- **Lattice Parameters**: Determining crystal structures
- **Surface Reconstructions**: Studying surface arrangements
- **Defect Structures**: Vacancies, interstitials, substitutions
- **Phase Transitions**: Structural transformations

### 3. Mechanical Properties

- **Elastic Constants**: Full elastic tensor
- **Bulk Modulus**: Compressibility
- **Phonon Calculations**: Vibrational properties
- **Thermal Expansion**: Temperature-dependent properties

### 4. Magnetic Properties

- **Collinear Magnetism**: Ferromagnetic/antiferromagnetic states
- **Non-Collinear Magnetism**: Complex spin arrangements
- **Spin-Orbit Coupling**: Relativistic effects
- **Magnetic Anisotropy**: Directional preferences

### 5. Optical Properties

- **Dielectric Functions**: Frequency-dependent response
- **Absorption Spectra**: Optical absorption
- **Reflectivity**: Surface optical properties
- **Electron Energy Loss**: EELS spectra

### 6. Advanced Calculations

- **GW Approximation**: Many-body corrections
- **BSE**: Bethe-Salpeter equation for excitons
- **RPA**: Random phase approximation
- **Hybrid Functionals**: HSE06, PBE0
- **Van der Waals**: DFT-D3, vdW-DF

## VASP vs MACE: Key Differences

| Aspect | VASP | MACE |
|--------|------|------|
| **Method** | Ab initio DFT | Machine Learning Potential |
| **Accuracy** | Reference quality | ~1-5 meV/atom from DFT |
| **Speed** | Hours to weeks | Seconds to minutes |
| **System Size** | ~100-1000 atoms | ~10,000-1,000,000 atoms |
| **Training Data** | Not required | Essential |
| **Properties** | All electronic properties | Energy, forces, stress |
| **Transferability** | Universal | Limited to training domain |
| **Cost** | Commercial licence | Open source |
| **Hardware** | HPC clusters | Single workstation possible |

### When to Use VASP

1. **New Systems**: Exploring unknown materials
2. **Electronic Properties**: Band gaps, DOS, charge densities
3. **High Accuracy**: Reference calculations
4. **Complex Properties**: Optical, magnetic, excited states
5. **Method Development**: Testing new functionals
6. **Publication Standards**: When DFT reference is required

### When to Use MACE

1. **Large Systems**: >1000 atoms
2. **Long Timescales**: Extended MD simulations
3. **High Throughput**: Screening many structures
4. **Known Chemistry**: Within training domain
5. **Finite Temperature**: Thermal properties
6. **Real-Time Applications**: Interactive simulations

## Technical Details

### Input Files

VASP requires four main input files:

```{tip}
Do note that these are by far non-exhaustive as VASP contains a list of lots of input parameters that can vary with workflows, materials and systems under study. For more information, refer to the VASP documentation at [VASP Wiki INCAR tags](https://www.vasp.at/wiki/index.php/Category:INCAR_tag).
```

1. **INCAR**: Calculation parameters 
```
SYSTEM = Silicon
ENCUT = 400
PREC = Accurate
ISMEAR = 0
SIGMA = 0.05
```

2. **POSCAR**: Crystal structure
```
Silicon
1.0
5.43 0.00 0.00
0.00 5.43 0.00
0.00 0.00 5.43
Si
8
Direct
0.00 0.00 0.00
0.25 0.25 0.25
...
```

3. **KPOINTS**: k-point sampling
```
Automatic mesh
0
Monkhorst-Pack
8 8 8
0 0 0
```

4. **POTCAR**: Pseudopotentials (provided with licence)

### Output Files

- **OUTCAR**: Detailed output
- **CONTCAR**: Final structure
- **EIGENVAL**: Eigenvalues
- **DOSCAR**: Density of states
- **CHGCAR**: Charge density
- **WAVECAR**: Wavefunctions

## Computational Workflow Comparison

### VASP Workflow
1. Prepare input files
2. Submit to HPC queue
3. Wait hours/days for completion
4. Post-process results
5. Analyse properties

### MACE Workflow
1. Load pre-trained model (or train custom model)
2. Run calculation (seconds/minutes)
3. Immediate results
4. Iterate rapidly
5. Use VASP for validation if needed

## Practical Considerations

### Computational Cost

**VASP Scaling**:

- CPU time ~ N³ (N = number of electrons)
- Memory ~ N²
- Typical calculation: 100-10,000 CPU hours

**MACE Scaling**:

- CPU time ~ N (N = number of atoms)
- Memory ~ N
- Typical calculation: 1-100 CPU hours

### Accuracy Considerations

**VASP**:

- Systematic errors from functional choice
- Convergence with respect to:
  - Plane-wave cutoff
  - k-point sampling
  - SCF tolerance

**MACE**:

- Errors from:
  - Training data quality
  - Model architecture
  - Extrapolation beyond training

## Integration Strategy

An effective approach often combines both methods:

1. **Initial Exploration**: Use MACE for rapid screening
2. **Refinement**: Validate interesting structures with VASP
3. **Training Data**: Generate VASP data for MACE training
4. **Property Calculation**: Use VASP for electronic properties
5. **Dynamics**: Use MACE for long MD trajectories

## Example: Studying a New Material

### Traditional VASP-Only Approach

1. Structure prediction (days-weeks)
2. Geometry optimisation (hours-days)
3. Property calculations (days)
4. Limited configurational sampling

### MACE-Accelerated Approach

1. Rapid structure search with MACE (hours)
2. Screen 1000s of configurations (hours)
3. Validate top candidates with VASP (days)
4. Train specialised MACE model
5. Extensive sampling and dynamics

## Licensing and Access

### VASP

- **Commercial Software**: Requires paid licence
- **Academic Licence**: ~€4000-5000 for group
- **Installation**: Complex, requires expertise
- **Support**: Professional support available

### MACE

- **Open Source**: MIT licence
- **Free**: No cost
- **Installation**: Simple pip install
- **Community**: Active development and support

## Future Perspectives

The future of materials modelling likely involves:

1. **Hybrid Workflows**: VASP for reference, MACE for production
2. **Active Learning**: MACE identifies where VASP calculations are needed
3. **Multi-Fidelity**: Combining different levels of theory
4. **Automated Workflows**: Seamless integration of both approaches

## Conclusion

VASP and MACE serve complementary roles in modern computational materials science:

- **VASP**: A standard tool for ab initio calculations, providing reference-quality results and access to all electronic properties
- **MACE**: Enables simulations at scales and timescales not feasible with DFT

Understanding when and how to use each tool is important for efficient materials research. Whilst VASP remains essential for electronic structure calculations and method validation, MACE provides new possibilities for large-scale simulations and rapid materials screening. The combination of these approaches represents a promising direction for computational materials discovery.