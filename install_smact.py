import os
import subprocess
import sys

def check_python_version():
    """
    Check if the Python version meets the minimum requirement.
    
    Raises:
        SystemError: If Python version is less than 3.9
    """
    if sys.version_info < (3, 9):
        raise SystemError("Python 3.9 or higher is required")

def create_virtual_environment():
    """
    Create a new virtual environment named 'smact-env' if it doesn't exist.
    
    The virtual environment is created using the venv module in the current directory.
    """
    if not os.path.exists("smact-env"):
        subprocess.run([sys.executable, "-m", "venv", "smact-env"])
        print("Created virtual environment: smact-env")

def install_requirements():
    """
    Install required packages from requirements.txt.
    
    Uses pip on Windows and pip3 on other operating systems.
    """
    pip_cmd = "pip" if os.name == "nt" else "pip3"
    subprocess.run([pip_cmd, "install", "-r", "requirements.txt"])
    print("Installed requirements")

def setup_smact():
    """
    Set up SMACT by cloning the repository and installing in development mode.
    
    1. Clones the SMACT repository if not present
    2. Changes to SMACT directory
    3. Installs SMACT in development mode
    4. Returns to original directory
    """
    # Clone SMACT repository if not present
    if not os.path.exists("SMACT"):
        subprocess.run(["git", "clone", "https://github.com/WMD-group/SMACT.git"])
        print("Cloned SMACT repository")
    
    # Install SMACT in development mode
    os.chdir("SMACT")
    subprocess.run([sys.executable, "setup.py", "develop"])
    os.chdir("..")
    print("Installed SMACT in development mode")

def main():
    """Main function to orchestrate the SMACT setup process."""
    print("Setting up SMACT environment...")
    check_python_version()
    create_virtual_environment()
    install_requirements()
    setup_smact()
    print("\nSetup complete! You can now activate the environment:")
    if os.name == "nt":
        print("    smact-env\\Scripts\\activate")
    else:
        print("    source smact-env/bin/activate")

if __name__ == "__main__":
    main()
