@echo off

:: Create and activate virtual environment
python -m venv smact-env
call smact-env\Scripts\activate

:: Install requirements
pip install -r requirements.txt

:: Clone and install SMACT if not present
if not exist SMACT (
    git clone https://github.com/WMD-group/SMACT.git
    cd SMACT
    pip install -e .
    cd ..
)

:: Setup pre-commit hooks
pre-commit install

echo Setup complete! Virtual environment is activated.
