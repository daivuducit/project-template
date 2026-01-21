"""Tests for the main module."""

import pytest
from {{ cookiecutter.pkg_name }} import main

def test_run_app_output(capsys):
    """
    Test the run_app function to ensure it prints the correct welcome message.
    'capsys' is a system fixture in pytest to capture stdout and stderr.
    """
    main.run_app()
    
    # Capture the output of the function call
    captured = capsys.readouterr()
    
    # Check if the expected strings are in the output
    assert "Welcome to {{ cookiecutter.project_name }}!" in captured.out
    assert "Developed by: {{ cookiecutter.full_name }}" in captured.out

def test_main_execution_logic():
    """
    Example of a basic logic test. 
    You can expand this as you add more features to main.py.
    """
    # Currently, run_app() returns None. We check if it executes without errors.
    assert main.run_app() is None