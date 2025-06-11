# Setup Instructions

This guide will help you set up your computational environment for the Materials Informatics course. We'll install SMACT, Chemeleon, and all necessary dependencies.

## What You'll Be Installing

- **SMACT**: The core toolkit for materials screening and structure prediction
- **Chemeleon**: AI-powered crystal structure generation tool
- **Jupyter**: For running interactive notebooks
- **Supporting Libraries**: NumPy, SciPy, pymatgen, pandas, and visualisation tools
- **Development Tools**: Pre-commit hooks for code quality (optional)

## Prerequisites

- **Python 3.9 or higher** (3.11 recommended)
- **Git** for cloning repositories
- **~2GB free disk space** for libraries and models
- **Internet connection** for downloading packages and pretrained models

## Quick Start (Automatic Installation)

We provide scripts that handle the entire setup process:

### For Unix/Mac Users:
```bash
# Make the script executable
chmod +x setup.sh

# Run the setup
./setup.sh
```

### For Windows Users:
```batch
# Run the setup script
setup.bat
```

These scripts will:
1. Create a virtual environment called `smact-env`
2. Install all required packages
3. Clone and install SMACT
4. Set up pre-commit hooks
5. Verify the installation

## Manual Installation

If you prefer to install manually or the automatic setup fails:

### 1. Create a Virtual Environment

```bash
# Create the environment
python -m venv smact-env

# Activate it
# On Unix/Mac:
source smact-env/bin/activate

# On Windows:
smact-env\Scripts\activate
```

### 2. Install Core Requirements

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

### 3. Install SMACT

```bash
# Clone the repository
git clone https://github.com/WMD-group/SMACT.git

# Install in development mode
cd SMACT
pip install -e .
cd ..
```

### 4. Install Chemeleon (Optional but Recommended)

```bash
# Clone the repository
git clone https://github.com/hspark1212/chemeleon-dng.git

# Install
cd chemeleon-dng
pip install -e .
cd ..
```

### 5. Set Up Development Tools (Optional)

```bash
# Install pre-commit hooks for code quality
pre-commit install
```

## Verifying Your Installation

Run the following commands to ensure everything is installed correctly:

```python
# Check SMACT
python -c "import smact; print(f'SMACT {smact.__version__} installed successfully')"

# Check key dependencies
python -c "import numpy, pandas, pymatgen, jupyter; print('All core dependencies installed')"

# Check if Chemeleon is available
python -c "try: import chemeleon_dng; print('Chemeleon installed successfully')
except: print('Chemeleon not installed (optional)')"
```

## Materials Project API Key

Some notebooks use data from the Materials Project. To access this data:

1. Register for a free account at [materialsproject.org](https://materialsproject.org)
2. Get your API key from your dashboard
3. Save it to `assets/files/mp_api_key.txt` or set it as an environment variable:
   ```bash
   export MP_API_KEY="your-key-here"  # Unix/Mac
   set MP_API_KEY=your-key-here       # Windows
   ```

## Running the Notebooks

Once setup is complete, you can start Jupyter:

```bash
# Make sure your virtual environment is activated
jupyter notebook

# Or use JupyterLab
jupyter lab
```

Navigate to any of the course notebooks and start learning!

## Troubleshooting

### Common Issues and Solutions

**1. Python Version Issues**
- Ensure you have Python 3.9+ by running `python --version`
- On some systems, you may need to use `python3` instead of `python`

**2. pip Installation Failures**
- Try upgrading pip: `pip install --upgrade pip`
- On Mac, you might need Xcode tools: `xcode-select --install`
- On Windows, you might need Visual C++ Build Tools

**3. Import Errors**
- Make sure your virtual environment is activated
- Try reinstalling the package that's failing to import

**4. Chemeleon Model Download Issues**
- The first run will download pretrained model checkpoints (~500MB)
- Ensure you have a stable internet connection
- Models are cached after first download

**5. Memory Issues**
- Some operations require 4GB+ RAM
- Close other applications if needed
- Use Google Colab for resource-intensive notebooks

## Alternative: Google Colab

If you have installation issues or limited computational resources, most notebooks can run on Google Colab:

1. Upload the notebook to Google Colab
2. Run the setup cell (included in each notebook)
3. Upload any required data files when prompted

## Getting Help

If you encounter issues:

1. Check the error message carefully - it often contains the solution
2. Search for the error online - many Python errors have known solutions
3. Review the [SMACT documentation](https://smact.readthedocs.io)
4. Open an issue on the course repository with:
   - Your operating system
   - Python version
   - The full error message
   - Steps you've tried

## Next Steps

After successful setup:
1. Test your installation by running the first notebook in "Combinatorial Explosion"
2. Familiarise yourself with Jupyter notebooks if needed
3. Review the course overview to understand the learning path

Happy materials discovery!
