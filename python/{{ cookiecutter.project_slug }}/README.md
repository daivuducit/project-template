# {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

## 🚀 Overview
This project was generated using a professional Python template designed for VS Code environments. It includes pre-configured tools for linting, formatting, and testing.

## 🛠 Installation

### 1. Prerequisite
Ensure you have **Python {{ cookiecutter.python_version }}** or higher installed.

### 2. Setup Virtual Environment
Step 1: Create a virtual environment
$ python -m venv .venv

Step 2: Activate the environment
# On Windows:
$ .venv\Scripts\activate
# On macOS/Linux:
$ source .venv/bin/activate

### 3. Install Dependencies
$ pip install -e ".[dev]"

> **Note:** After creating the `.venv`, VS Code should automatically detect the Python interpreter. If not, press `Ctrl+Shift+P` -> `Python: Select Interpreter` and choose the one inside `.venv`.
## 💻 Development Workflow

### Linting & Formatting
We use Ruff for fast linting and formatting. Configuration is in pyproject.toml.
- Check errors: ruff check .
- Auto-fix & Format: ruff check . --fix && ruff format .

### Running Tests
We use pytest for testing.
- Run all tests: pytest
- Run with coverage: pytest --cov=src

## 📁 Project Structure
- src/: Main source code.
- tests/: Unit and integration tests.
- .vscode/: Pre-configured IDE settings.
- .env/: Environment variables (not tracked by Git).

---
* **Author**: {{ cookiecutter.full_name }} (<{{ cookiecutter.email }}>)
* **GitHub**: [{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})
* **License**: {{ cookiecutter.license }}
* **Version**: {{ cookiecutter.version }}