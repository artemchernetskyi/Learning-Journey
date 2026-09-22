from pathlib import Path


current_directory = Path.cwd()

print(f"Current directory: {current_directory}")
print(f"Data type: {type(current_directory)}")

lesson_directory = Path("DevOps") / "Python" / "lesson_06"
script_path = lesson_directory / "path_basics.py"

print(f"Lesson directory: {lesson_directory}")
print(f"Script path: {script_path}")
print(f"Is absolute: {lesson_directory.is_absolute()}")
print(f"Directory exists: {lesson_directory.exists()}")
print(f"Script exists: {script_path.exists()}")

full_script_path = current_directory / script_path
resolved_script_path = script_path.resolve()

print(f"Full script path: {full_script_path}")
print(f"Resolved script path: {resolved_script_path}")
print(f"Is full path absolute: {full_script_path.is_absolute()}")
print(f"Paths are equal: {full_script_path == resolved_script_path}")

print(f"File name: {script_path.name}")
print(f"File stem: {script_path.stem}")
print(f"File suffix: {script_path.suffix}")
print(f"Parent directory: {script_path.parent}")