def create_environment_files():
    """Generate .env and .gitignore files."""
    with open(".env", "w") as f:
        f.write("# Environment variables go here\n")
    
    with open(".gitignore", "w") as f:
        f.write(".venv/\n__pycache__/\n.env\n*.pyc\n")

if __name__ == "__main__":
    create_environment_files()
