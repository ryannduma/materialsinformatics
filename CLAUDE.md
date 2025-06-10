# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jupyter Book educational project for teaching Materials Informatics using SMACT (Semiconducting Materials by Analogy and Chemical Theory). The project creates an interactive web-based textbook with theoretical content (Markdown) and practical exercises (Jupyter notebooks).

## Key Commands

### Building the Book
```bash
# Build the Jupyter Book
jupyter-book build .

# Clean build directory before rebuilding
jupyter-book clean .
```

### Development Environment Setup
```bash
# Unix/Mac automatic setup
chmod +x setup.sh && ./setup.sh

# Windows automatic setup
setup.bat

# Alternative: Python setup script
python install_smact.py
```

### Code Quality and Testing
```bash
# Install pre-commit hooks (required for development)
pre-commit install

# Run pre-commit checks on all files
pre-commit run --all-files

# Run tests
pytest

# Run tests with coverage
pytest --cov
```

### Working with Notebooks
```bash
# Create student versions of notebooks (removes solution blocks)
python assets/files/make_blank_nb.py <input_notebook.ipynb> <output_notebook.ipynb>
```

## Architecture and Structure

### Content Organization
The course is organized into modules, each containing:
- `intro.md`: Module introduction and theory
- `follow along notebook.ipynb`: Hands-on exercises with code
- Supporting data files (CSV, database files)

### Key Configuration Files
- `_config.yml`: Jupyter Book configuration (execution settings, MyST extensions)
- `_toc.yml`: Table of contents defining book structure
- `requirements.txt`: Python dependencies including smact>=2.8
- `.pre-commit-config.yaml`: Automated code quality checks (Ruff, prettier, nbstripout)

### Development Workflow
1. Virtual environment: `smact-env` (created by setup scripts)
2. Pre-commit hooks enforce code quality (Ruff formatting/linting, notebook output stripping)
3. Notebooks are executed with 300s timeout and results are cached
4. Build outputs go to `_build/` directory

## Important Notes

- Always run pre-commit hooks before committing changes
- Notebook outputs should be stripped (handled automatically by pre-commit)
- The project uses Ruff for Python code formatting and linting
- API keys (like Materials Project) should be stored in `assets/files/mp_api_key.txt`, never in code
- When modifying notebooks, ensure they work both locally and on Google Colab

## Code Style Guidelines

### Language and Spelling
- **British English**: All content, comments, documentation, and output messages must use British English spelling and terminology
- Examples: "colour" not "color", "analyse" not "analyze", "optimise" not "optimize", "centre" not "center"
- Use British terminology: "whilst" instead of "while", "amongst" instead of "among" where appropriate

### Tone and Style
- **Natural and engaging**: Write in a conversational yet professional tone that feels natural to read
- **Grounded approach**: Avoid hyperbole, exaggerations, or overly enthusiastic language
- **Balanced enthusiasm**: Show genuine interest in the subject matter without being overly excited
- **Educational focus**: Maintain clarity and accessibility while keeping content intellectually honest
- Examples of what to avoid: "Amazing!", "Incredible!", "Mind-blowing!", excessive exclamation marks
- Examples of good tone: "This approach works well", "An effective method", "This demonstrates clearly"

### Emojis and Output Formatting
- **NO EMOJIS in code**: Do not use emojis in print statements, comments, or any generated code
- Use clear, professional text for all output messages
- Example of what NOT to do: `print("✓ Success!")` 
- Example of what to do: `print("Success!")` or `print("PASSED: Test completed successfully")`
- Keep all code output clean and professional for educational content