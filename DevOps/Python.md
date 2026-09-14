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

---

## Python Lesson 01 — Variables, Data Types, Input, Conversion, and Arithmetic Operators

Date: `2026-09-14`

Status: **Completed**

Today I learned how to store values, inspect their types, convert text input to numbers, and calculate simple DevOps results.

### Objective

Use variables, basic data types, `input()`, conversion, `print()`, f-strings, comparisons, and arithmetic operators to write two small programs about servers and containers.

### Environment

- Used the existing repository interpreter: `.venv/bin/python`.
- Python version: `3.12.3`.
- VS Code selected **Learning-Journey (3.12.3)**.
- No packages were installed, no system Python packages were modified, and no network requests were made.
- No `uv init` was run and no `pyproject.toml` was created.

During documentation, this command confirmed the interpreter version:

```bash
.venv/bin/python --version
```

```text
Python 3.12.3
```

### Variables and basic data types

A variable is a name that refers to a value. Assignment uses `=`. `type()` shows the type of a value.

Examples matching the completed practice:

```python
name = "Artem"
age = 19
docker_score = 9.0
monitoring_enabled = True

print(type(name))
print(type(age))
print(type(docker_score))
print(type(monitoring_enabled))
```

Results:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

| Type | Example | Meaning |
|---|---|---|
| `str` | `"Artem"` | Text, also called a string. |
| `int` | `19` | A whole number. |
| `float` | `9.0` | A floating-point number. |
| `bool` | `True` | A Boolean value: `True` or `False`. |

Python uses **dynamic typing**: I do not declare a fixed type for a variable, and I can reassign it to a value of another type. Values have types. `True` and `False` are Boolean values; `"True"` with quotation marks is a string.

### Strings, numbers, and conversion

I reassigned `docker_score` from the float `9.0` to the string `"9.0"`:

```python
docker_score = 9.0
docker_score = "9.0"
print(docker_score + " points")
```

Result:

```text
9.0 points
```

Here, `+` concatenates (joins) two strings. The intentional attempt to add an integer to that string failed:

```python
docker_score + 1
```

```text
TypeError: can only concatenate str (not "int") to str
```

I converted the string with `float()` and then added `1`:

```python
print(float(docker_score))
print(float(docker_score) + 1)
print(type(docker_score))
```

Results:

```text
9.0
10.0
<class 'str'>
```

Conversion returns a new value. Calling `float(docker_score)` does not automatically change the original variable; `docker_score` still refers to the string `"9.0"`. To retain a converted value, assign the result to a variable.

### input(), conversion, and readable output

`input()` always returns `str`, even when I type digits. In the server program:

```python
running_containers_text = input("Enter the number of running containers: ")
running_containers = int(running_containers_text)
```

Typing `3` gives the string `"3"`; `int(running_containers_text)` converts it from **str → int**. Disk usage is converted in the same way. The text variable remains a string, and the new variable stores the integer.

`print()` displays output. An f-string inserts values inside `{}` into readable text:

```python
print(f"Running containers: {running_containers}")
```

With `running_containers = 3`, this prints `Running containers: 3`. A standalone `print()` prints a blank line.

### Independent DevOps practice — variables and input

File: [variables_and_input.py](Python/lesson_01/variables_and_input.py)

My program asks for a server name and running-container count, converts the count to an integer, stores `monitoring_enabled = True`, and calculates the count after one additional deployment. It then asks for disk usage, converts it to an integer, and compares it with `warning_threshold = 80` using `>=`.

This uses entered example values; it does not inspect a real server or deploy a container.

Complete source, preserved from my existing file:

```python
server_name = input("Enter the server name: ")
running_containers_text = input("Enter the number of running containers: ")

running_containers = int(running_containers_text)
monitoring_enabled = True
containers_after_deployment = running_containers + 1

print(f"Server: {server_name}")
print(f"Running containers: {running_containers}")
print(f"Monitoring enabled: {monitoring_enabled}")
print(f"Containers after deployment: {containers_after_deployment}")

print()

disk_usage_text = input("Enter disk usage percentage: ")
disk_usage = int(disk_usage_text)
warning_threshold = 80
disk_warning = disk_usage >= warning_threshold

print(f"Disk usage: {disk_usage}%")
print(f"Warning threshold: {warning_threshold}%")
print(f"Disk warning: {disk_warning}")
```

Run interactively from the repository root:

```bash
.venv/bin/python DevOps/Python/lesson_01/variables_and_input.py
```

Verified lesson results:

| Server | Running containers | After deployment | Disk usage | Threshold | Disk warning |
|---|---|---|---|---|---|
| `web-01` | `3` | `4` | `85%` | `80%` | `True` |
| `web-01` | `3` | `4` | `80%` | `80%` | `True` |

During documentation, the boundary test was rerun safely with:

```bash
printf 'web-01\n3\n80\n' | .venv/bin/python DevOps/Python/lesson_01/variables_and_input.py
```

**Linux review:** `printf` supplies three newline-separated answers, and the pipe passes them to the program's standard input. Piped answers are not echoed like typed terminal input, so prompts appear on the same lines as later output.

Exact verified output, with exit code `0`:

```text
Enter the server name: Enter the number of running containers: Server: web-01
Running containers: 3
Monitoring enabled: True
Containers after deployment: 4

Enter disk usage percentage: Disk usage: 80%
Warning threshold: 80%
Disk warning: True
```

I initially thought `80 >= 80` would be `False`. The correction is **True**: `>=` means **greater than or equal to**, so the threshold itself triggers the warning.

### Arithmetic operators

File: [arithmetic_operators.py](Python/lesson_01/arithmetic_operators.py)

I used `cpu_cores = 4`, `containers_per_core = 3`, and `running_containers = 10` to calculate capacity and distribute containers into groups.

| Operator | Meaning | Lesson calculation | Result |
|---|---|---|---|
| `*` | Multiplication | `4 * 3` | `12` total capacity |
| `-` | Subtraction | `12 - 10` | `2` free slots |
| `/` | Regular division | `10 / 4` | `2.5` average per core |
| `//` | Floor division | `10 // 4` | `2` complete groups |
| `%` | Remainder | `10 % 4` | `2` remaining items |

Floor division rounds the quotient down. For these positive integers, it gives the number of complete groups. The remainder is the number of items left after forming those groups:

```text
10 / 4 = 2.5
10 // 4 = 2 complete groups
10 % 4 = 2 remaining items
10 = (4 * 2) + 2
```

I initially confused the fractional part `0.5` with the remainder. **0.5 is not numerically equal to 2.** Half of a group of four corresponds to two remaining containers: `0.5 * 4 = 2`.

Complete source, preserved from my existing file:

```python
cpu_cores = 4
containers_per_core = 3
running_containers = 10

total_capacity = cpu_cores * containers_per_core
free_slots = total_capacity - running_containers
average_per_core = running_containers / cpu_cores
full_groups = running_containers // cpu_cores
remaining_containers = running_containers % cpu_cores

print(f"Total capacity: {total_capacity}")
print(f"Free slots: {free_slots}")
print(f"Average per core: {average_per_core}")
print(f"Full groups: {full_groups}")
print(f"Remaining containers: {remaining_containers}")
```

Run from the repository root:

```bash
.venv/bin/python DevOps/Python/lesson_01/arithmetic_operators.py
```

Exact verified output during documentation, with exit code `0`:

```text
Total capacity: 12
Free slots: 2
Average per core: 2.5
Full groups: 2
Remaining containers: 2
```

### Assessment and corrections

Final knowledge check: **4/5 before correction**.

Correct knowledge confirmed during the check:

- `"12"` is `str`.
- `12` is `int`.
- `12.0` is `float`.
- `False` is `bool`.
- `input()` returns `str`.
- Conversion creates a new value; it does not automatically change the original variable.
- `80 >= 80` is `True`.

The only final-check mistake was describing `int()` in the wrong direction. For this program, `int(running_containers_text)` converts **str → int**, not int → str.

The arithmetic explanation was correct after clarifying the difference between the fractional part of a quotient and the remainder. The earlier threshold and remainder misconceptions were corrected during the lesson; they are separate from the one final-check mistake.

### Important vocabulary

| Word or phrase | Simple meaning | Ukrainian |
|---|---|---|
| variable | A name that refers to a value. | змінна |
| data type | The kind of value, such as text or an integer. | тип даних |
| string | Text represented by `str`. | рядок |
| integer | A whole number. | ціле число |
| floating-point number | A number represented by `float`, such as `9.0`. | число з рухомою комою |
| Boolean | A `True` or `False` value. | булеве значення |
| dynamic typing | A variable can be reassigned to values of different types. | динамічна типізація |
| concatenate | Join strings together. | об'єднувати рядки |
| convert | Produce a value of another type. | перетворювати |
| input / output | Data entered into / displayed by a program. | введення / виведення |
| threshold | A limit used for a comparison or warning. | поріг |
| greater than or equal to | At least the compared value: `>=`. | більше або дорівнює |
| floor division | Division with the quotient rounded down. | ділення з округленням донизу |
| remainder | Items left after forming complete groups. | остача |
| deployment | Putting an application into service. | розгортання |

Useful technical-English sentences:

- `input() returns a string.`
- `I converted the container count from a string to an integer.`
- `The disk warning is true because disk usage is greater than or equal to the threshold.`
- `Ten containers form two complete groups of four, with two containers remaining.`

### Completion checklist

- [x] Use the existing repository Python 3.12.3 environment.
- [x] Practise `str`, `int`, `float`, `bool`, and `type()`.
- [x] Explain dynamic typing and Boolean values versus quoted strings.
- [x] Reassign a value, concatenate strings, and explain the intentional `TypeError`.
- [x] Convert `"9.0"` with `float()` and obtain `10.0` after adding `1`.
- [x] Explain that conversion returns a new value.
- [x] Use `input()`, `int()`, `print()`, and f-strings in independent practice.
- [x] Verify the disk warning at `85%` and at the exact `80%` threshold.
- [x] Practise `*`, `-`, `/`, `//`, and `%` and explain the verified results.
- [x] Complete the final knowledge check with `4/5` before correction and correct the conversion direction.
- [x] Inspect and rerun both source files successfully during documentation, preserving their contents.
- [x] Install nothing and leave system Python packages unchanged.

### Next step

**Python Lesson 02** is next and has not started. The short optional Linux administration refresher remains after **Python Lesson 05**.

### My sentence

I used Python variables, converted text input to integers, and calculated container capacity and a disk warning.
