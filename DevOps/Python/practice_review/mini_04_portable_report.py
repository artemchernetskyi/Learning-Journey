from pathlib import Path


report_lines = [
    "web-api: READY",
    "worker: WARNING",
    "database: CRITICAL",
    "cache: READY",
]

script_directory = Path(__file__).resolve().parent
report_path = script_directory / "review_report.txt"

report_content = "\n".join(report_lines) + "\n"
report_path.write_text(report_content, encoding="utf-8")

saved_lines = report_path.read_text(encoding="utf-8").splitlines()

print(f"Report path: {report_path}")
print(f"File exists: {report_path.exists()}")
print(f"Saved lines: {len(saved_lines)}")
print("Report:")

for line in saved_lines:
    print(f"- {line}")