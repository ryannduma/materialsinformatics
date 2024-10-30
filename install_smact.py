import os
import subprocess
import sys

def check_python_version():
    if sys.version_info < (3, 9):
        raise SystemError("Python 3.9 or higher is required")

def create_virtual_environment():
    if not os.path.exists("smact-env"):
        subprocess.run([sys.executable, "-m", "venv", "smact-env"])
        print("Created virtual environment: smact-env")

def install_requirements():
    pip_cmd = "pip" if os.name == "nt" else "pip3"
    subprocess.run([pip_cmd, "install", "-r", "requirements.txt"])
    print("Installed requirements")

def setup_smact():
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
