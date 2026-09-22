from pathlib import Path


report_path = Path("DevOps/Python/lesson_06/deployment_report.txt")
new_entry = "cache: READY"

if report_path.exists():
    report_lines = report_path.read_text(encoding="utf-8").splitlines()
else:
    report_lines = []

if new_entry not in report_lines:
    with report_path.open("a", encoding="utf-8") as report_file:
        report_file.write(f"{new_entry}\n")

    print(f"Added: {new_entry}")
else:
    print(f"Already exists: {new_entry}")

print("Current deployment report:")
print(report_path.read_text(encoding="utf-8"))