import os
import subprocess

def init_git():
    """Initialize git and add all files."""
    try:
        subprocess.run(['git', 'init'], check=True)
        print(">>> Git initialized successfully.")
    except Exception as e:
        print(f"Could not initialize git: {e}")

def create_environment_files():
    """Create .env and .gitignore files if they don't exist."""
    with open(".env", "w") as f:
        f.write("# Environment variables go here\n")
    
    with open(".gitignore", "w") as f:
        f.write(".venv/\n__pycache__/\n.env\n*.pyc\n")

if __name__ == "__main__":
    create_environment_files()
    init_git()