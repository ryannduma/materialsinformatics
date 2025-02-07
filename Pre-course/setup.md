# Setup Instructions

This guide will help you set up your environment for the Materials Informatics course.

## Prerequisites

1. Python 3.9 or higher
2. Git
3. A text editor or IDE
4. Command line interface

## Installation Steps

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

After installation, verify everything is working:

```python
python -c "import smact; print(smact.__version__)"
```

## Getting Help

If you encounter any issues during setup:

1. Check the error messages
2. Consult the troubleshooting guide
3. Ask for help in the course forum
4. Contact the course instructors
