# Python Notes — Artem

## Purpose

This file contains my Python for DevOps notes.

The goal is to learn Python step by step, practise real commands, and explain scripts in clear English.

---

## Python Setup / Lesson 00 — Environment and first program

Date: `2026-09-13`

Status: **Completed**

Today I prepared my Python learning environment and ran my first Python program in the terminal and VS Code.

### Objective

Use a project virtual environment based on Ubuntu's Python, verify which interpreter runs my code, and practise a small calculation without changing the system Python package environment.

The setup results below were verified during the completed lesson. Installation and environment-creation commands are recorded as history; they were not repeated during documentation.

### Main concepts and tool roles

| Component | Role in this setup |
|---|---|
| System interpreter: `/usr/bin/python3` | Ubuntu's Python 3.12.3; the base interpreter used to create the virtual environment. |
| `venv` | Python's standard-library module for creating virtual environments; it is available on this system. |
| `pip` | A Python package installer. The system installation reported version 24.0; no system package installation was performed. |
| `uv` | A tool for Python environment and package management. I used it to create `.venv`. |
| Virtual environment: `.venv` | A directory at the repository root with a separate Python package environment. It uses system Python as its base. |
| Virtual-environment interpreter: `.venv/bin/python` | The executable that runs my lesson program using the project environment. |
| VS Code | The editor that edits and organizes my files. |
| Nano | Another text editor, used in the terminal. Saving a file in Nano does not execute it. |
| Microsoft Python extension | Connects VS Code to the selected Python interpreter and provides Python tooling. |

The system interpreter and project interpreter both report Python `3.12.3`. Their paths and environment prefixes distinguish them. Using system Python as a base does not mean installing packages into its package environment.

### System environment

Verified environment:

- Ubuntu `24.04`.
- System Python: `Python 3.12.3`.
- System interpreter: `/usr/bin/python3`.
- The `venv` module is available.

The command:

```bash
python3 -m pip --version
```

reported `pip 24.0` from the Ubuntu system installation. Here, `-m pip` runs the `pip` module with the selected `python3` interpreter, and `--version` reports version information without installing a package.

No package was installed into the system Python environment.

### Installing uv

`uv` was initially absent. I installed it with the official Astral standalone installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

`curl` downloads the installer, and the pipe passes it to `sh` for execution. The options follow redirects (`-L`), suppress the progress meter (`-s`), show errors (`-S`), and fail on HTTP error responses (`-f`).

Verified installation results:

| Item | Result |
|---|---|
| uv version | `0.12.13` |
| uv path | `/home/artem/.local/bin/uv` |
| uvx path | `/home/artem/.local/bin/uvx` |

No `sudo` or global `pip` was used.

### Creating and activating the virtual environment

From the repository root, I created the environment with:

```bash
uv venv --python /usr/bin/python3
```

`uv venv` creates a virtual environment. `--python /usr/bin/python3` explicitly selects Ubuntu's interpreter as the base. The environment directory is `.venv` at the repository root.

I activated it with:

```bash
source .venv/bin/activate
```

**Linux review:** `source` runs the activation script in the current shell. Activation changes the shell's environment so that `python` resolves to the project interpreter. The prompt displayed `(Learning-Journey)`.

Verified values inside the environment:

| Check | Result |
|---|---|
| Python version | `3.12.3` |
| `sys.executable` | `/home/artem/Projects/Learning-Journey/.venv/bin/python` |
| `sys.prefix` | `/home/artem/Projects/Learning-Journey/.venv` |
| `sys.base_prefix` | `/usr` |

`sys.prefix` identifies the active environment. `sys.base_prefix` identifies its base Python installation. The different prefixes confirm that this interpreter is using a virtual environment.

The root `.gitignore` already contains `.venv/`. The environment stays local and is not tracked in Git.

We intentionally did not run `uv init` or create `pyproject.toml` yet. No third-party Python packages were installed.

### Python REPL practice

The REPL is Python's interactive prompt: read, evaluate, print, loop. It runs Python statements as I enter them.

I created integer variables for `19` Linux lessons and `12` Docker lessons, added them, and printed `31`. I practised:

- variable assignment with `=`;
- integer addition with `+`;
- displaying a result with `print()`;
- inserting a value into text with an f-string: `f"Completed lessons: {completed_lessons}"`.

The names and calculation preserved in my first file are:

```python
linux_lessons = 19
docker_lessons = 12
completed_lessons = linux_lessons + docker_lessons
```

I exited the REPL with:

```python
exit()
```

### First Python file

File: [first_program.py](Python/lesson_00/first_program.py)

I used Nano as a terminal text editor. The saved program imports the standard-library `sys` module, calculates `19 + 12`, prints the interpreter path and completed-lesson total, and prints `Python for DevOps starts now.`

From the repository root, the program can be run explicitly with the project interpreter:

```bash
.venv/bin/python DevOps/Python/lesson_00/first_program.py
```

An explicit interpreter path also works without activating the shell. The Python executable runs the file; the editor only saves its contents.

During documentation, the existing file was inspected and preserved without rewriting. It was safely rerun with:

```bash
.venv/bin/python -I -B DevOps/Python/lesson_00/first_program.py
```

`-I` isolates execution from Python environment variables and user import paths. `-B` prevents bytecode-cache writes.

Verified output, with exit code `0`:

```text
Python executable: /home/artem/Projects/Learning-Journey/.venv/bin/python
Completed lessons: 31
Python for DevOps starts now.
```

### VS Code setup

I installed the official Microsoft Python extension. The installed components reported:

| Extension ID | Version |
|---|---|
| `ms-python.vscode-python-envs` | `1.36.0` |
| `ms-python.debugpy` | `2026.6.0` |
| `ms-python.python` | `2026.4.0` |
| `ms-python.vscode-pylance` | `2026.3.1` |

I selected `./.venv/bin/python` as the workspace interpreter. VS Code successfully ran `first_program.py` with that interpreter.

The workflow is: edit and organize the file in VS Code → use the Python extension with the selected interpreter → execute the program with `.venv/bin/python`.

### Common mistakes and distinctions

These are mistakes to avoid, not a record of additional failed commands:

- Assuming the version alone proves that the virtual environment is active. Check `sys.executable` and the prefixes as well.
- Confusing the `.venv` directory with the executable `.venv/bin/python` inside it.
- Assuming shell activation also selects the VS Code workspace interpreter. Verify the selection in VS Code separately.
- Expecting Nano or the Python extension itself to execute Python code. The selected Python interpreter executes it.
- Entering shell commands at the Python REPL prompt. Use `exit()` to return to the shell first.
- Treating `uv venv` as `uv init`. This lesson created an environment without initializing project metadata.
- Using system `pip` to install lesson dependencies. This setup left the system package environment unchanged.

### Important vocabulary

| Word | Simple meaning | Ukrainian |
|---|---|---|
| interpreter | A program that executes Python code. | інтерпретатор |
| virtual environment | A separate Python package environment for a project. | віртуальне середовище |
| editor | A program used to change text files. | текстовий редактор |
| extension | A component that adds features to an editor. | розширення |
| integer | A whole number, such as `19`. | ціле число |
| assignment | Giving a variable a value with `=`. | присвоєння |
| execute | Run a program. | виконувати |

### Completion checklist

- [x] Verify Ubuntu, system Python, system pip, and venv availability.
- [x] Install uv without sudo or global pip.
- [x] Create and activate the repository `.venv` using `/usr/bin/python3`.
- [x] Verify the interpreter path, version, and environment prefixes.
- [x] Keep `.venv/` ignored by Git.
- [x] Practise variables, integer addition, `print()`, and an f-string in the REPL.
- [x] Exit the REPL with `exit()`.
- [x] Create and successfully run the first Python file.
- [x] Select the virtual-environment interpreter in VS Code and run the file successfully.
- [x] Leave the system package environment unchanged; install no third-party Python packages.
- [x] Complete Setup / Lesson 00 without running `uv init` or creating `pyproject.toml`.

### Next step

**Python Lesson 01** is next and has not started. The short optional Linux administration refresher remains after **Python Lesson 05**.

### My sentence

I set up a virtual environment and ran my first Python program with the project interpreter.
