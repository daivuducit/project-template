# import subprocess
# import os
# import sys

# # def init_git():
# #     """Intialize a git repository."""
# #     try:
# #         subprocess.run(['git', 'init'], check=True)
# #         print(">>> Git initialized successfully.")
# #     except Exception as e:
# #         print(f"Could not initialize git: {e}")

def create_environment_files():
    """Generate .env and .gitignore files."""
    with open(".env", "w") as f:
        f.write("# Environment variables go here\n")
    
    with open(".gitignore", "w") as f:
        f.write(".venv/\n__pycache__/\n.env\n*.pyc\n")

# # def create_venv():
# #     """
# #     Generate a virtual environment using the specified Python interpreter.
# #     """
# #     actual_python = "{{ cookiecutter.actual_python_path }}"
    
# #     print(f">>> Creating virtual environment (.venv) using: {actual_python}")
# #     try:
# #         subprocess.run([actual_python, '-m', 'venv', '.venv'], check=True)
# #         print(">>> Virtual environment created successfully.")
# #     except Exception as e:
# #         print(f"Could not create virtual environment: {e}")

if __name__ == "__main__":
    create_environment_files()
#     # init_git()
#     # create_venv()