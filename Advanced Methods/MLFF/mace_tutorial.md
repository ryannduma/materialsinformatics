# MACE Tutorial: A Practical Guide to Machine Learning Force Fields

## Introduction

MACE (Multi-Atomic Cluster Expansion) is an advanced machine learning interatomic potential framework that enables efficient molecular simulations. Unlike traditional quantum mechanical methods such as VASP, MACE uses neural networks to predict atomic forces and energies, offering significantly improved computational speeds whilst maintaining accuracy comparable to DFT calculations.

## Key Differences from VASP

Before exploring MACE in detail, it is useful to understand how it differs from VASP:

| Aspect | VASP | MACE |
|--------|------|------|
| **Method** | Ab initio DFT calculations | Machine learning potentials |
| **Speed** | Slow (hours to days) | Fast (seconds to minutes) |
| **System Size** | Limited (~100s atoms) | Large (~100,000s atoms) |
| **Accuracy** | Ground truth | ~1-5 meV/atom from DFT |
| **Training Required** | No | Yes |
| **Transferability** | Universal | Limited to training domain |
| **Licence** | Commercial | Open source |

## Installation

### Prerequisites
- Python 3.8 or higher
- PyTorch (with CUDA support for GPU acceleration)

### Installing MACE

```bash
# Clone the repository
git clone https://github.com/ACEsuit/mace.git
cd mace

# Install via pip
pip install .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Verify Installation

```python
import mace
print(mace.__version__)
```

## Quick Start: Using Pre-trained Models

MACE provides several pre-trained foundation models that can be used immediately without training:

### 1. Loading a Foundation Model

```python
from mace.calculators import mace_mp

# Load the MACE-MP medium model
calc = mace_mp(model="medium", device="cuda")  # Use "cpu" if no GPU

# Attach to an ASE atoms object
from ase.io import read
atoms = read("structure.xyz")
atoms.calc = calc

# Calculate energy and forces
energy = atoms.get_potential_energy()
forces = atoms.get_forces()
print(f"Energy: {energy:.3f} eV")
print(f"Forces shape: {forces.shape}")
```

### 2. Running Molecular Dynamics

```python
from ase import units
from ase.md.nvtberendsen import NVTBerendsen
from ase.io.trajectory import Trajectory

# Set up MD simulation
dyn = NVTBerendsen(atoms, 
                   timestep=1.0 * units.fs,
                   temperature_K=300,
                   taut=0.1 * units.picosecond)

# Attach trajectory writer
traj = Trajectory("md_trajectory.traj", "w", atoms)
dyn.attach(traj.write, interval=10)

# Run for 1000 steps
dyn.run(1000)
```

## Training Your Own MACE Model

When foundation models aren't suitable for your specific system, you can train a custom MACE model:

### 1. Preparing Training Data

MACE requires structures with energies and forces. The data should be in ASE-readable format:

```python
from ase.io import read, write
import numpy as np

# Read DFT calculations (e.g., from VASP)
structures = read("OUTCAR", index=":")  # Reads all configurations

# Save as XYZ with extended properties
write("training_data.xyz", structures)
```

### 2. Configuration File

Create a configuration file `config.yaml`:

```yaml
# Basic training configuration
seed: 123
name: "my_mace_model"

# Model architecture
hidden_irreps: "128x0e + 128x1o"
r_max: 5.0
num_radial_basis: 8
num_cutoff_basis: 5
max_ell: 3
num_interactions: 2

# Training settings
batch_size: 10
max_num_epochs: 1000
learning_rate: 0.01
patience: 50
eval_interval: 10

# Data
train_file: "training_data.xyz"
valid_fraction: 0.1
test_fraction: 0.1

# Loss weights
energy_weight: 1.0
forces_weight: 100.0
```

### 3. Training the Model

```bash
mace_run_train \
    --name="my_model" \
    --train_file="training_data.xyz" \
    --valid_fraction=0.1 \
    --test_fraction=0.1 \
    --config_type_weights='{"Default":1.0}' \
    --E0s="average" \
    --model="MACE" \
    --hidden_irreps="128x0e + 128x1o" \
    --r_max=5.0 \
    --batch_size=10 \
    --max_num_epochs=1000 \
    --device=cuda
```

### 4. Using Your Trained Model

```python
from mace.calculators import MACECalculator

# Load your trained model
calc = MACECalculator(
    model_paths="my_model.model",
    device="cuda"
)

# Use it like any ASE calculator
atoms.calc = calc
energy = atoms.get_potential_energy()
```

## Practical Example: Geometry Optimisation

```python
from ase.optimize import BFGS
from ase.io import read, write

# Read structure
atoms = read("initial_structure.cif")

# Attach MACE calculator
calc = mace_mp(model="medium", device="cuda")
atoms.calc = calc

# Optimise geometry
opt = BFGS(atoms, logfile="optimisation.log")
opt.run(fmax=0.01)  # Force convergence criterion in eV/Å

# Save optimised structure
write("optimised_structure.cif", atoms)

# Print results
print(f"Initial energy: {atoms.get_potential_energy():.3f} eV")
print(f"Final energy: {atoms.get_potential_energy():.3f} eV")
```

## Advanced Features

### 1. Uncertainty Quantification

MACE can provide uncertainty estimates using committee models:

```python
# Train a committee of models
for i in range(5):
    os.system(f"mace_run_train --name=model_{i} --seed={i} ...")

# Use committee for predictions
from mace.calculators import MACECommitteeCalculator

calc = MACECommitteeCalculator(
    model_paths=[f"model_{i}.model" for i in range(5)]
)

# Get uncertainty estimates
atoms.calc = calc
energy_mean = atoms.get_potential_energy()
energy_std = calc.results["energy_uncertainty"]
```

### 2. Active Learning

MACE supports active learning workflows to efficiently expand training datasets:

```python
# Identify structures with high uncertainty
uncertainties = []
for structure in candidate_structures:
    structure.calc = calc
    energy = structure.get_potential_energy()
    uncertainties.append(calc.results["energy_uncertainty"])

# Select most uncertain structures for DFT calculations
indices = np.argsort(uncertainties)[-10:]  # Top 10 most uncertain
selected_structures = [candidate_structures[i] for i in indices]
```

## Best Practices

1. **Data Quality**: Ensure your training data covers the relevant configuration space
2. **Validation**: Always validate on structures not seen during training
3. **Cutoff Radius**: Choose r_max based on your system (typically 5-6 Å)
4. **Model Size**: Start with smaller models and increase complexity if needed
5. **Force Matching**: Weight forces heavily in the loss function (typically 10-100x energy weight)

## Troubleshooting

### Common Issues

1. **Out of Memory**: Reduce batch size or model size
2. **Poor Forces**: Increase force weight in loss function
3. **Overfitting**: Add more training data or reduce model complexity
4. **Slow Training**: Use GPU acceleration or reduce cutoff radius

### Performance Tips

- Use GPU acceleration for both training and inference
- Compile models with TorchScript for production use
- Use neighborlists for large-scale simulations
- Consider using mixed precision training

## Conclusion

MACE provides a comprehensive framework for accelerating materials simulations whilst maintaining accuracy comparable to DFT methods. After completing this tutorial, you should be able to:

- Use pre-trained MACE models for immediate calculations
- Train custom models for your specific systems
- Perform geometry optimisations and molecular dynamics
- Implement uncertainty quantification and active learning

For more advanced topics and updates, refer to the [official MACE documentation](https://github.com/ACEsuit/mace).