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

---

## Python Lesson 02 — Conditional Statements and Boolean Logic

Date: `2026-09-14`

Status: **Completed**.

Today I learned how to combine conditions and choose a resource or service status. The final disk and service verification runs matched the completed lesson results below.

### Objective

Use `if`, `elif`, `else`, comparisons, and Boolean logic in [disk_status.py](Python/lesson_02/disk_status.py) and [service_health.py](Python/lesson_02/service_health.py). These programs use entered example values rather than checking live infrastructure.

### Conditional statements and priority

`if` checks the first condition. `elif` checks another condition if earlier conditions were false. `else` runs when none of the preceding conditions matched.

The colon `:` introduces a block. Indentation is Python syntax: this lesson uses four spaces to indent each block. Python checks an `if`/`elif`/`else` chain from top to bottom. Only the first true branch executes; later branches are skipped even if their conditions would also be true. Condition order therefore establishes status priority.

```python
disk_usage = 95
if disk_usage >= 90:
    print("CRITICAL")
elif disk_usage >= 80:
    print("WARNING")
else:
    print("OK")
```

Expected output: `CRITICAL`. Both comparisons would be true, but the first matching branch prevents the warning branch from executing.

### Comparisons, assignment, and Boolean expressions

The lesson conditions evaluate to Boolean `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `<` | Is less than | `75 < 80` | `True` |
| `>=` | Is greater than or equal to | `80 >= 80` | `True` |
| `==` | Is equal to | `0 == 0` | `True` |

`=` assigns/stores a value. `==` compares two values and returns `True` or `False`. A comparison does not change the compared variable. Its result can be assigned to a separate Boolean variable:

```python
running_replicas = 3
is_ready = running_replicas == 3
print(running_replicas)
print(is_ready)
print(type(is_ready))
```

Expected output:

```text
3
True
<class 'bool'>
```

| Boolean operator | Meaning for Boolean conditions | Example | Result |
|---|---|---|---|
| `and` | All connected conditions must be true. | `False and True` | `False` |
| `or` | At least one connected condition must be true. | `False or True` | `True` |
| `not` | Reverses a Boolean value. | `not False` | `True` |

A Boolean expression can be assigned to a variable such as `service_healthy`. For Boolean variables, `if maintenance_mode:` and `elif not service_healthy:` are clearer than explicitly writing `is True` or `is False`.

Ordinary assignment and `print()` statements execute from top to bottom. A preceding Boolean variable does not automatically control them; a conditional statement and its indented block provide that control.

### Disk and resource exercise

Both `disk_usage` and `cpu_usage` use `int(input(...))` to convert input strings to integers.

The source calculates:

```python
both_resources_normal = disk_usage < 80 and cpu_usage < 80
maintenance_mode = False
alerts_enabled = not maintenance_mode
```

Both resources must be below `80` for `both_resources_normal` to be `True`. `alerts_enabled` is `True` because `not False` is `True`.

**Alerts enabled** means the alerting mechanism is active; it does not mean a warning was triggered. In this script, `alerts_enabled` is printed but does not guard the status block. The disk status chain checks resource usage directly.

The CRITICAL threshold is `90`; the WARNING threshold is `80`. Either resource reaching a threshold is sufficient because the conditions use `or`. CRITICAL is checked before WARNING, followed by the `else` OK branch.

Lesson results, also verified during documentation:

| Disk | CPU | `both_resources_normal` | `alerts_enabled` | Exact status message |
|---|---|---|---|---|
| `70` | `75` | `True` | `True` | `OK: Resource usage is normal.` |
| `85` | `75` | `False` | `True` | `WARNING: Resource usage is high.` |
| `70` | `95` | `False` | `True` | `CRITICAL: Resource usage is very high.` |

For `70` disk and `95` CPU, the critical condition is `70 >= 90 or 95 >= 90`: `False or True` is `True`.

Expected result lines for `70` and `75`, excluding input prompts:

```text
Both resources normal: True
Alerts enabled: True
OK: Resource usage is normal.
```

### Service-health exercise

The program reads `service_name` as a string and converts `running_replicas` and `error_rate` to integers. Health requires at least three replicas, an error rate below ten, and maintenance mode disabled:

```python
service_healthy = running_replicas >= 3 and error_rate < 10 and not maintenance_mode
```

All three conditions must be true. Service status priority is:

1. **MAINTENANCE** when `maintenance_mode` is true.
2. **CRITICAL** when `running_replicas == 0 or error_rate >= 50`.
3. **WARNING** when `not service_healthy`.
4. **OK/HEALTHY** in the final `else` block.

The lesson called the successful outcome HEALTHY; the inspected source prints `OK: Service web-api is healthy.` for that branch. F-strings insert the dynamic `service_name` into the service display and CRITICAL, WARNING, and OK messages instead of hard-coding `web-api`. The maintenance message is simply `MAINTENANCE.`.

Reported completed lesson results for service `web-api`:

| Replicas | Error rate | Maintenance mode | `service_healthy` | Status |
|---|---|---|---|---|
| `3` | `5` | `False` | `True` | HEALTHY (`OK: Service web-api is healthy.`) |
| `2` | `5` | `False` | `False` | `WARNING: Service web-api is experiencing issues.` |
| `0` | `5` | `False` | `False` | `CRITICAL: Service web-api requires immediate attention.` |
| `0` | `99` | Temporarily `True` | `False` | `MAINTENANCE.` |

During the lesson, `maintenance_mode` was temporarily set to `True`. Even with `0` replicas and error rate `99`, the result was `MAINTENANCE.`: maintenance was the first true branch, so it prevented the later critical branch from executing. This temporary test was not recreated during documentation.

`maintenance_mode` was restored to `False` afterward. Reinspection confirmed `maintenance_mode = False` in the final `service_health.py`. The three final non-maintenance verification cases reproduced the expected OK, WARNING, and CRITICAL results. Neither Python source file was modified during this documentation correction.

### Workspace-path correction

During the lesson, the first copies were accidentally created under `/home/artem/DevOps` because VS Code was opened from the home directory. Those copies used `/usr/bin/python3`.

The correct files were copied into the Learning-Journey repository and run using `/home/artem/Projects/Learning-Journey/.venv/bin/python`. The two accidental external copies were moved to Ubuntu Trash and the empty `/home/artem/DevOps` directory was removed. Only the repository files remain relevant.

This is the reported cleanup history. Documentation work stayed inside the repository and did not inspect or repeat the external cleanup.

### Assessment and corrected misconceptions

Final knowledge check: **4/5 before clarification**. Notes were allowed; the assessment focused on understanding rather than memorization.

I correctly understood conditional branches, status priority, thresholds, and the service-status cases. Boolean-expression composition and the exact distinction between `=` and `==` required clarification. After correction, I correctly identified `is_ready` as `bool` and explained the core logic.

Corrections to retain:

- An enabled alerting mechanism does not mean an alert has fired.
- A Boolean variable does not automatically control the assignments or print statements after it.
- `False and True` is `False`; `False or True` is `True`; `not False` is `True`.
- Comparisons return a result without changing the compared variable; the result can be stored separately.
- The first matching branch prevents later true branches from executing.
- Use **condition**, rather than “equals,” to describe a Boolean expression.
- Say **is less than** for numeric `<` and **Python executes the block** when explaining control flow.

### Documentation verification

Both source files were inspected completely and hashed with `sha256sum` before execution. All runs used only `/home/artem/Projects/Learning-Journey/.venv/bin/python`, with `-I` for isolated execution and `-B` to prevent bytecode-cache writes. Newline-separated input was supplied non-interactively.

Example command from the repository root:

```bash
printf '70\n75\n' | /home/artem/Projects/Learning-Journey/.venv/bin/python -I -B DevOps/Python/lesson_02/disk_status.py
```

**Linux review:** the pipe passes `printf` output to the script's standard input. Input prompts appear together because piped answers are not echoed as typed terminal input.

| Script | Inputs | Exit code | Rerun result |
|---|---|---|---|
| `disk_status.py` | `70`, `75` | `0` | `True`, alerts `True`, OK; matches lesson. |
| `disk_status.py` | `85`, `75` | `0` | `False`, alerts `True`, WARNING; matches lesson. |
| `disk_status.py` | `70`, `95` | `0` | `False`, alerts `True`, CRITICAL; matches lesson. |
| `service_health.py` | `web-api`, `3`, `5` | `0` | `True`, OK; matches lesson. |
| `service_health.py` | `web-api`, `2`, `5` | `0` | `False`, WARNING; matches lesson. |
| `service_health.py` | `web-api`, `0`, `5` | `0` | `False`, CRITICAL; matches lesson. |

Exact final service output for `web-api`, `3`, and `5`:

```text
service_name: running_replicas: error_rate: Service: web-api
Service healthy: True
OK: Service web-api is healthy.
```

SHA-256 values of the current source files before correction verification, unchanged afterward:

```text
e1ccaef4c2fbff7c03ee69752904c9b1a245d8864787a6e872cf8285bc9fdcf4  DevOps/Python/lesson_02/disk_status.py
26f9f488d661411aa4deb6f18ff8a17ae15e0f3c905c35e9b6038aeb973241bf  DevOps/Python/lesson_02/service_health.py
```

No source files were modified. Nothing was installed, no network requests were made, and nothing was staged, committed, or pushed. `source-backup.tar.gz` was not inspected or modified.

### Important vocabulary

| Word or phrase | Simple meaning | Ukrainian |
|---|---|---|
| condition | An expression checked to decide what happens. | умова |
| branch | One possible path through conditional code. | гілка |
| colon | The `:` character that introduces the block here. | двокрапка |
| indentation | Spaces at the start of a line that mark a block. | відступ |
| Boolean expression | An expression that produces `True` or `False` here. | булевий вираз |
| assignment | Storing a value using `=`. | присвоєння |
| comparison | Comparing values using operators such as `<` or `==`. | порівняння |
| threshold | A boundary used to select a status. | поріг |
| priority | Which condition is checked first. | пріоритет |
| maintenance mode | A state used during planned service work. | режим обслуговування |
| replica | A running copy of a service. | репліка / копія сервісу |
| enabled | Active or switched on. | увімкнений |

### Completion checklist

- [x] Practise `if`, `elif`, `else`, colons, and four-space indentation.
- [x] Explain comparisons, Boolean values, `and`, `or`, and `not`.
- [x] Distinguish assignment `=` from comparison `==`.
- [x] Explain the `80 >= 80` boundary and first-match status priority.
- [x] Complete disk/resource and service-health exercises and review the maintenance case.
- [x] Use dynamic service names in f-strings.
- [x] Correct the workspace path and record the reported external-copy cleanup.
- [x] Complete the knowledge check at `4/5` before clarification and explain the corrected logic.
- [x] Inspect both sources, run six cases with exit code `0`, and preserve both SHA-256 hashes.
- [x] Confirm `maintenance_mode = False` in the final service source and reproduce the expected OK, WARNING, and CRITICAL results.

### My sentence

- Python checks each condition from top to bottom and executes the block for the first true condition.
- Both resources are normal when disk usage is less than 80 and CPU usage is less than 80.
- Alerts are enabled, but this does not mean a warning was triggered.
- The service is healthy when it has at least three replicas, its error rate is below ten, and maintenance mode is disabled.
- I use `=` to assign a value and `==` to compare two values. The comparison result is a Boolean.

### Next step

**Python Lesson 03** is next and has not started. The short optional Linux administration refresher remains after **Python Lesson 05**.

---

## Python Lesson 03 — Collections and DevOps Data Structures

Date: `2026-09-16`

Status: **Completed**

Today I learned how to choose and use lists, tuples, sets, dictionaries, and nested collections for DevOps data. I combined all four collection types in an independent deployment validator.

### Objective

Store changing sequences, fixed allowed values, unique package names, keyed service configuration, and nested server data in suitable Python collections. Use indexing, slicing, membership, collection methods, set operations, and Boolean expressions to validate a deployment.

### Collection comparison

| Collection | Syntax example | Ordered | Mutable | Duplicates | Main access style | Good lesson use |
|---|---|---|---|---|---|---|
| List | `["web-01", "db-01"]` | Yes | Yes | Yes | Numeric index or slice | A changing deployment queue |
| Tuple | `("staging", "production")` | Yes | No | Yes | Numeric index or slice | Fixed allowed environments |
| Set | `{"docker", "curl"}` | No reliable order | Yes, through methods | No | Membership and set operations | Unique installed packages |
| Dictionary | `{"name": "web-01", "active": True}` | Preserves insertion order | Yes | Keys must be unique | Key | Named server settings |

### Lists

A list is ordered and mutable, and it supports duplicate values. Lists use square brackets. Indexing begins at `0`, and the negative index `-1` accesses the final element. Indexing returns one element, while slicing returns a new list.

```python
servers = ["web-01", "web-02", "db-01"]
first_server = servers[0]
last_server = servers[-1]
first_two = servers[0:2]
```

The slice `[0:2]` includes the elements at indexes `0` and `1`, but excludes index `2`. `len(servers)` returns the number of elements. The expression `"db-01" in servers` performs a membership check and returns a Boolean. `append()` adds an element to the end, and `remove()` removes a matching value.

Accessing an index that does not exist would raise `IndexError`. A list with four elements has indexes `0` through `3`; it has four elements, not “four indexes.” List changes happen sequentially, so each mutation affects later results.

#### Server inventory

File: [server_inventory.py](Python/lesson_03/server_inventory.py)

The initial list was `web-01`, `web-02`, and `db-01`. The program printed the complete list, its list type, and the elements at indexes `0`, `1`, and `2`.

It then replaced `web-02` with `web-02-prod` and appended `cache-01`. At that point, the list contained four elements. The program removed `db-01` only after confirming that it was present. The later membership check stored `False` in `db_server_active`.

The remaining list contained `web-01`, `web-02-prod`, and `cache-01`. The first element was `web-01`, the last element accessed with `-1` was `cache-01`, and the `[0:2]` slice returned `web-01` and `web-02-prod`.

Expected final result lines:

```text
['web-01', 'web-02-prod', 'cache-01']
Is db-01 active: False
Total servers: 3
First server: web-01
Last server: cache-01
Web servers: ['web-01', 'web-02-prod']
```

#### Deployment queue

File: [deployment_queue.py](Python/lesson_03/deployment_queue.py)

This was an independent list exercise completed without receiving a full solution. The initial targets were `dev-01`, `staging-01`, and `prod-01`. I replaced the first target with `dev-02`, appended `backup-01`, and removed `staging-01` after a membership check.

`production_available` became `True`. The final list was `dev-02`, `prod-01`, and `backup-01`. The first target was `dev-02`, the last target was `backup-01`, the first-two slice contained `dev-02` and `prod-01`, and the length was `3`.

```text
Removed server: staging-01
Is prod-01 available: True
First target: dev-02
Last target: backup-01
Priority targets: ['dev-02', 'prod-01']
Total targets: 3
```

I initially used the generic variable name `servers` instead of the requested `deployment_targets`. After clarification, I used VS Code **Rename Symbol** to rename every occurrence correctly. Exact variable-name requirements matter in real automation because other code, tests, configuration, or team members may depend on an agreed interface.

### Tuples

A tuple is ordered and indexed like a list, but it is immutable. Tuples use parentheses. They support indexing, negative indexing, `len()`, slicing, and membership checks. Existing tuple elements cannot be replaced, added, or removed.

File: [infrastructure_config.py](Python/lesson_03/infrastructure_config.py)

```python
environments = ("development", "staging", "production")
```

The first environment was `development`, the last was `production`, the count was `3`, and the membership check for `production` was `True`.

The intentional line:

```python
environments[0] = "dev"
```

produced:

```text
TypeError: 'tuple' object does not support item assignment
```

The line attempted to replace an existing element; it did not attempt to add an element. The failing line was then kept as a comment with an explanation, so the final program exits successfully.

Expected final output:

```text
('development', 'staging', 'production')
<class 'tuple'>
First environment: development
Last environment: production
Environment count: 3
Production exists: True
```

### Sets

A set contains unique values. Sets are unordered, so their printed order may vary, and they do not support indexing. Duplicate source values are automatically collapsed. Sets are mutable through methods such as `add()` and `discard()`.

`discard()` safely does nothing when a value is absent. By contrast, `remove()` can raise an error when the requested value is absent. `len()` counts unique values.

```python
missing = required_packages - installed_packages  # In required, but not installed
common = installed_packages & required_packages   # In both sets
all_packages = installed_packages | required_packages  # In either set
```

An empty set displays as `set()`. The syntax `{}` creates an empty dictionary, not an empty set.

#### Package sets

File: [package_sets.py](Python/lesson_03/package_sets.py)

`installed_packages` initially included `nginx` twice in the source, plus `docker` and `curl`. The duplicate was stored only once, so the initial unique count was `3`. Docker membership was `True`.

`required_packages` contained `docker`, `curl`, `git`, and `python3`. The set calculations produced these semantic results; the printed order is allowed to vary:

| Calculation | Result |
|---|---|
| Required minus installed | `git`, `python3` |
| Installed minus required | `nginx` |
| Intersection | `docker`, `curl` |
| Union | `nginx`, `docker`, `curl`, `git`, `python3` |

The program later added `git` to `installed_packages` and discarded `nginx`. The updated installed set contained `docker`, `curl`, and `git`.

The original `missing_packages` variable still contained `git` and `python3` because it stored the earlier calculation. Python variables are not automatically updating spreadsheet formulas. A new calculation stored only `python3` in `updated_missing_packages`.

Representative output, with set order allowed to differ:

```text
Package count: 3
Docker installed: True
Missing packages: {'git', 'python3'}
Extra packages: {'nginx'}
Common packages: {'docker', 'curl'}
Updated installed packages: {'docker', 'curl', 'git'}
Original missing packages: {'git', 'python3'}
Updated missing packages: {'python3'}
```

### Dictionaries

A dictionary stores key-value pairs. Dictionaries use braces, colons between keys and values, and commas between pairs. Values may have different data types. Data is accessed by keys rather than numeric indexes.

```python
server = {"name": "web-01", "port": 8080, "active": True}
server["port"] = 9090
region = server.get("region", "not configured")
```

`len(dictionary)` counts key-value pairs. Assigning to an existing key updates its value, while assigning to a new key adds a pair. `in` checks key membership. `get(key, default)` safely returns the default when a key is absent. Direct access to an absent key would raise `KeyError`. `pop(key)` removes the pair and returns its value.

#### Server configuration

File: [server_config.py](Python/lesson_03/server_config.py)

The initial fields were name `web-01`, IP `10.0.0.10`, port `8080`, and active `True`. The initial dictionary length was `4`.

The program updated the port to `9090`, updated active to `False`, and added environment `production`. Updating existing keys did not increase the length; adding `environment` increased it to `5`. The comparison stored Boolean `True` in `is_production`, not the string `"production"`.

`get()` returned `not configured` for the absent `region` key. IP membership was `True` before removal. `pop("ip")` removed the pair and returned the string `10.0.0.10`. IP membership was `False` afterward, and the final dictionary length was `4`.

Expected result lines:

```text
Server name: web-01
Server IP: 10.0.0.10
Server port: 8080
Server active: True
Configuration fields: 4
Updated port: 9090
Server active: False
Environment: production
Is production: True
Configuration fields: 5
Region: not configured
IP existed before removal: True
Removed IP: 10.0.0.10
IP exists after removal: False
Configuration fields: 4
```

### Nested collections

A list can contain dictionaries. In `server_fleet[0]["name"]`, Python first selects the list element at index `0` and then accesses the `name` key in that dictionary.

File: [server_fleet.py](Python/lesson_03/server_fleet.py)

`server_fleet` was a list, and `server_fleet[0]` was a dictionary. The primary server was `web-01`, the database server was `db-01`, and `database_ready` was `False`. Therefore, the `else` branch printed `Database status: WARNING`.

```text
<class 'list'>
<class 'dict'>
Primary server: web-01
Database server: db-01
Database ready: False
Database status: WARNING
```

A collection's contents and the result of `type()` are different: printing `server_fleet` shows its contents, while `type(server_fleet)` returns its data type.

### Deployment validator

File: [deployment_validator.py](Python/lesson_03/deployment_validator.py)

The deployment validator was the Lesson 03 practical integration task. I completed it independently without loops, functions, or imports.

Its data is:

- `allowed_environments`: a tuple containing `staging` and `production`;
- `required_packages`: a set containing `docker`, `curl`, and `git`;
- final `installed_packages`: a set containing `docker`, `curl`, and `nginx`;
- `deployment_queue`: a list containing `web-api`, `worker`, and `cache`;
- `service`: a dictionary with name `web-api`, environment `production`, `3` running replicas, `2` required replicas, and active `True`.

The program calculates `missing_packages` with set difference. `environment_allowed` uses tuple membership. `replicas_ready` compares running and required replicas. `packages_ready` checks whether `len(missing_packages) == 0`. `service_queued` uses list membership.

The final check combines every result and `service["active"]` with `and`:

```python
deployment_ready = (
    environment_allowed
    and replicas_ready
    and packages_ready
    and service_queued
    and service["active"]
)
```

All connected conditions must be `True`. In the final scenario, `packages_ready` is `False`, so one false value makes the entire `and` expression `False`.

Final expected result, with the one-element set representing missing `git`:

```text
Missing packages: {'git'}
Environment allowed: True
Replicas ready: True
Packages ready: False
Service queued: True
Deployment ready: False
Deployment status: BLOCKED
```

During the lesson, `git` was temporarily added to `installed_packages`. The observed READY-path test produced:

```text
Missing packages: set()
Packages ready: True
Deployment ready: True
Deployment status: READY
```

`git` was then removed again to restore the final BLOCKED scenario. The final source includes a comment explaining that `git` can be added to test READY. The long `deployment_ready` expression was reformatted across multiple lines, diagnostic output was placed before the final READY/BLOCKED status, and unnecessary f-string prefixes were removed from the static status messages.

### Corrected misconceptions and clarifications

- Set duplicates are stored only once, so four source entries can produce a length of `3`.
- Sets do not have reliable indexes.
- Intersection means values present in both sets, not all values.
- A tuple item assignment attempts to replace an element; it does not add an element.
- Use **elements**, rather than “variables,” when describing tuple contents.
- `len(dictionary)` returns the number of key-value pairs, not the dictionary's values.
- `pop()` returns the removed value, not a Boolean.
- A comparison such as `environment == "production"` returns `True` or `False`.
- `type(collection)` returns the data type, not the collection contents.
- List modifications happen sequentially and change later results.
- A list suits a changing deployment queue; a tuple suits fixed allowed values.
- An empty set is `set()`, while `{}` is an empty dictionary.
- Variables keep calculated results until they are explicitly recalculated.

### Assessment

The final deployment validator was completed independently and produced correct results. The initial final knowledge-check result was approximately **4.5/6 before clarification**. Notes and existing lesson files were allowed; the assessment focused on understanding rather than memorization.

Strong areas:

- set difference, intersection, and union after correction;
- tuple immutability;
- nested list/dictionary access;
- membership checks;
- combining Boolean checks into deployment status;
- understanding why the deployment was blocked and how adding `git` changed it to READY.

Clarification was needed for:

- mapping a list versus a tuple to changing versus fixed data;
- distinguishing `type()` results from collection contents;
- calculating the final list after sequential mutations;
- remembering that `len(dictionary)` returns a number;
- remembering that `pop()` returns the removed value;
- recognizing that `is_production` stores a Boolean.

After targeted corrections, I correctly explained that a deployment queue requires a list because `staging-01` could be removed, while a tuple would be immutable. The Lesson 03 knowledge check was **passed after clarification**.

### Parallel course note

I purchased the Udemy course **Python for DevOps: Mastering Real-World Automation**. I will use it as parallel reinforcement, while the Learning-Journey lessons remain my primary structured practice. Course exercises should remain separate unless I independently rewrite them into original portfolio work.

### Important vocabulary

| Word or phrase | Simple meaning | Ukrainian |
|---|---|---|
| collection | A value that groups other values. | колекція |
| element | One value stored in a collection. | елемент |
| ordered | Stored with a defined sequence. | впорядкований |
| mutable | Can be changed after creation. | змінюваний |
| immutable | Cannot be changed after creation. | незмінюваний |
| index | A numeric position in an ordered collection. | індекс |
| slice | A new sequence selected from part of another sequence. | зріз |
| membership | Whether a value or key is present. | належність / наявність |
| unique | Present only once. | унікальний |
| intersection | Values present in both sets. | перетин |
| union | Values present in either set. | об'єднання |
| key-value pair | A named key and its associated value. | пара ключ-значення |
| nested collection | A collection stored inside another collection. | вкладена колекція |
| recalculate | Calculate again using current values. | перерахувати |

### My sentences

- A set stores only unique values, is unordered, and does not support indexing.
- After a tuple is created, we cannot replace, add, or remove its elements.
- Deployment is blocked because `git` is required but is not installed.
- We need to add `git` to `installed_packages` to make the deployment ready.
- We removed `staging-01` from the deployment queue. We could not do this with a tuple because tuples are immutable.
- The comparison returns a Boolean, and assignment stores that result in the variable.

### Completion checklist

- [x] Practise list indexing, negative indexing, slicing, membership, mutation, `append()`, `remove()`, and `len()`.
- [x] Complete the independent deployment-queue exercise and correct the requested variable name.
- [x] Practise tuple access and explain the intentional immutability `TypeError`.
- [x] Practise unique set values, membership, `add()`, `discard()`, difference, intersection, and union.
- [x] Explain why an earlier set calculation does not update automatically.
- [x] Practise dictionary access, updates, additions, `get()`, `pop()`, membership, and length.
- [x] Access dictionaries nested inside a list and select the WARNING branch.
- [x] Complete the deployment validator independently and explain every Boolean check.
- [x] Observe both the BLOCKED final path and the temporary READY path.
- [x] Pass the Lesson 03 knowledge check after targeted clarification.
- [x] Inspect all seven final source files, verify successful execution, and preserve their contents and SHA-256 hashes.

### Next step

**Python Lesson 04** is next and has not started. The short optional Linux administration refresher remains after **Python Lesson 05**.
