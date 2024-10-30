# SMACT Materials Informatics Tutorial Series

This repository contains a series of Jupyter notebooks designed to teach materials informatics using SMACT (Semiconducting Materials by Analogy and Chemical Theory).

## Getting Started

### Automatic Installation
1. For Unix/Mac users:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. For Windows users:
   ```batch
   setup.bat
   ```

### Manual Installation
1. Create a virtual environment:
   ```bash
   python -m venv smact-env
   source smact-env/bin/activate  # On Windows: smact-env\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Clone and install SMACT:
   ```bash
   git clone https://github.com/WMD-group/SMACT.git
   cd SMACT
   pip install -e .
   cd ..
   ```

4. Setup pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Verifying Installation
After installation, you can verify everything is working by running:
```python
python -c "import smact; print(smact.__version__)"
```


## Finally you can open the `00_Introduction_and_Setup.ipynb` notebook to begin the tutorial series.

## Course Structure

1. Introduction and Setup
2. Combinatorial Explosion
3. Chemical Filters
4. Compositional Screening
5. Stoichiometry Screening
6. Structure Prediction
7. Advanced Methods

## Requirements

- Python 3.7+
- SMACT
- Other dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- SMACT developers and contributors
- Hyunsoo Park for writing and sharing the CHEMELEON module
