# ugit - Build Your Own Git

A Python implementation of Git, built from scratch as a learning project. This project follows the "Build Your Own X" philosophy to understand how version control systems work under the hood.

## Project Overview

`ugit` is a simplified implementation of Git that demonstrates the core concepts of version control systems. By building git from scratch, we'll learn about:

- Object storage and hashing
- Commit history and branching
- Working directory management
- Remote repository operations

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Project Setup

#### 1.1 Create Virtual Environment

Create a Python virtual environment to isolate project dependencies:

```bash
python3 -m venv venv
```

#### 1.2 Activate Virtual Environment

Activate the virtual environment:

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You'll know the virtual environment is active when you see `(venv)` at the beginning of your terminal prompt.

#### 1.3 Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

This installs:
- `click` - CLI framework for building command-line interfaces
- `pytest` - Testing framework
- `black` - Code formatter (optional)
- `flake8` - Linter (optional)

#### 1.4 Install setuptools

Install setuptools and wheel for package management:

```bash
pip install setuptools wheel
```

#### 1.5 Install Project in Development Mode

Install the `ugit` package in editable/development mode:

```bash
pip install -e .
```

This makes the `ugit` command available from anywhere (when the venv is activated) and links it to your local code, so changes are immediately reflected.

### Step 2: Verify Installation

Test that everything is working by running:

```bash
ugit
```

You should see:
```
Hello, World!
```

Congratulations! The project is set up and ready for development.

## Project Structure

```
ugit/
├── venv/              # Virtual environment (not committed to git)
├── cli.py             # Main CLI entry point
├── setup.py           # Package configuration
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Development

### Running the CLI

After installation, you can run `ugit` from anywhere (with venv activated):

```bash
ugit
```

### Deactivating Virtual Environment

When you're done working, deactivate the virtual environment:

```bash
deactivate
```

**Note:** Remember to activate the virtual environment (`source venv/bin/activate`) each time you start a new terminal session.

## Next Steps

- [ ] Implement basic git commands (init, add, commit)
- [ ] Add object storage system
- [ ] Implement commit history
- [ ] Add branching and merging
- [ ] Implement remote operations

## License

This is an educational project built for learning purposes.
