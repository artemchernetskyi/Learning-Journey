from pathlib import Path


lesson_directory = Path("DevOps/Python/lesson_06")
reports_directory = lesson_directory / "reports"

reports_directory.mkdir(parents=True, exist_ok=True)

python_files = sorted(lesson_directory.glob("*.py"))

print(f"Reports directory: {reports_directory}")
print(f"Directory exists: {reports_directory.exists()}")
print("Python files:")

for python_file in python_files:
    print(f"- {python_file.name}")

print(f"Total Python files: {len(python_files)}")