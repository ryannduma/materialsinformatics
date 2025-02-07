# SMACT Structure Prediction Module

This module provides tools for predicting new crystal structures based on ionic substitutions, implementing the methodology described in:

> Hautier, G., Fischer, C., Ehrlacher, V., Jain, A., and Ceder, G. (2011)  
> Data Mined Ionic Substitutions for the Discovery of New Compounds.  
> Materials Chemistry, ChemRxiv, 2024.  
> [doi:10.26434/chemrxiv-2024-rw8p5](https://doi.org/10.26434/chemrxiv-2024-rw8p5)

## Overview

The structure prediction module enables the prediction of new crystal structures through statistical analysis of known structures and ionic substitutions. It uses a database of known structures (typically from ICSD via the Materials Project) and a probability model for ionic substitutions to suggest new, potentially stable compounds.

## Module Components

### 1. Structure Module (`structure.py`)

The core module containing the `SmactStructure` class, which provides a minimalist structure representation for manipulation and analysis.

Key features:
- POSCAR-style structure specification
- Integration with Materials Project
- Structure manipulation and analysis tools
- Conversion to/from pymatgen structures

Main functions:
- `from_file()`: Create structure from POSCAR file
- `from_mp()`: Create structure from Materials Project data
- `from_py_struct()`: Convert from pymatgen structure
- `composition()`: Generate composition string
- `as_poscar()`: Convert to POSCAR format
- `as_py_struct()`: Convert to pymatgen structure

### 2. Mutation Module (`mutation.py`)

Contains the `CationMutator` class for handling species substitutions in crystal structures.

Key features:
- Lambda table management for substitution probabilities
- Structure mutation operations
- Probability calculations for substitutions

Main functions:
- `from_json()`: Create mutator from JSON lambda table
- `sub_prob()`: Calculate substitution probability
- `cond_sub_prob()`: Calculate conditional substitution probability
- `unary_substitute()`: Generate structures with single substitutions
- `_mutate_structure()`: Perform species mutation
- `_nary_mutate_structure()`: Perform multiple species mutations

### 3. Prediction Module (`prediction.py`)

Implements the `StructurePredictor` class for generating new structure predictions.

Key features:
- Structure prediction based on statistical analysis
- Support for single and multiple species substitutions
- Probability thresholding for predictions

Main functions:
- `predict_structs()`: Predict structures for given species
- `nary_predict_structs()`: Predict structures with multiple substitutions

### 4. Database Module (`database.py`)

Provides the `StructureDB` class for managing structure databases.

Key features:
- SQLite database interface
- Materials Project integration
- Parallel processing support

Main functions:
- `add_mp_icsd()`: Add Materials Project ICSD structures
- `add_struct()`: Add single structure
- `add_structs()`: Add multiple structures
- `get_structs()`: Retrieve structures by composition
- `get_with_species()`: Retrieve structures containing specific species

### 5. Probability Models Module (`probability_models.py`)

Contains models for calculating substitution probabilities.

Key features:
- Base `SubstitutionModel` class
- `RadiusModel` implementation using Shannon radii

Main functions:
- `sub_prob()`: Calculate substitution probability
- `gen_lambda()`: Generate lambda table

### 6. Utilities Module (`utilities.py`)

Provides helper functions for data parsing and manipulation.

Key functions:
- `parse_spec()`: Parse species string
- `unparse_spec()`: Convert species tuple to string
- `get_sign()`: Get string representation of charge sign

## Usage Examples

### Basic Structure Creation
```python
from smact.structure_prediction import SmactStructure

# Create from POSCAR file
structure = SmactStructure.from_file("path/to/POSCAR")

# Create from Materials Project
structure = SmactStructure.from_mp(
    species=[("Fe", 2), ("O", -2)],
    api_key="YOUR_MP_API_KEY"
)
```

### Structure Prediction
```python
from smact.structure_prediction import (
    StructurePredictor,
    CationMutator,
    StructureDB
)

# Initialize components
mutator = CationMutator.from_json()
db = StructureDB("structures.db")
predictor = StructurePredictor(mutator, db, "structures")

# Predict structures
species = [("Fe", 2), ("O", -2)]
predictions = predictor.predict_structs(
    species,
    thresh=1e-3,
    include_same=True
)

# Process predictions
for structure, probability, parent in predictions:
    print(f"Predicted structure with probability: {probability}")
    print(structure.as_poscar())
```

### Database Management
```python
from smact.structure_prediction import StructureDB

# Create database
db = StructureDB("structures.db")

# Add Materials Project structures
num_added = db.add_mp_icsd(
    table="icsd_structures",
    mp_api_key="YOUR_MP_API_KEY"
)

# Retrieve structures
structures = db.get_with_species(
    species=[("Fe", 2), ("O", -2)],
    table="icsd_structures"
)
```

## Installation

The module requires the following dependencies:
- pymatgen
- numpy
- pandas
- pathos (optional, for parallel processing)

## Notes

- The module uses Shannon radii data for the default probability model
- Parallel processing is available when pathos is installed
- API keys for Materials Project are required for MP integration
- The database can be memory-based (":memory:") or file-based
